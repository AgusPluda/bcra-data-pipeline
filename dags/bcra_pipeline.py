# Corre airflow en http://localhost:8080/

from datetime import datetime

import psycopg
import requests
from airflow.hooks.base import BaseHook
from airflow.sdk import dag, task


@dag(
    dag_id="bcra_pipeline",
    start_date=datetime(2026, 8, 1),
    schedule="@daily",
    catchup=False,
)
def bcra_pipeline():

    @task
    def extract_bcra(id_variable):
        results = requests.get(
            f"https://api.bcra.gob.ar/estadisticas/v4.0/monetarias/{id_variable}?desde=2026-08-01&hasta=2026-08-28"
        )
        results_json = results.json()
        if results.status_code == 200:
            lista_detalle = results_json["results"][0]["detalle"]
            # Ingresar id_variable
            for fila in lista_detalle:
                fila["id_variable"] = results_json["results"][0]["idVariable"]
            print(len(lista_detalle))
            return lista_detalle
        else:
            raise ValueError(
                f"Status code no exitoso (status_code={results.status_code})"
            )

    @task
    def load_raw(lista_detalle):
        conn_info = BaseHook.get_connection("warehouse_pg")

        with psycopg.connect(
            host=conn_info.host,
            port=conn_info.port,
            dbname=conn_info.schema,
            user=conn_info.login,
            password=conn_info.password,
        ) as pg_conn:
            with pg_conn.cursor() as cur:
                for fila in lista_detalle:
                    cur.execute(
                        """
                        INSERT INTO raw.bcra_series (id_variable, fecha, valor)
                        VALUES (%s, %s, %s)
                        ON CONFLICT (id_variable, fecha) DO UPDATE
                            SET valor = EXCLUDED.valor,
                                loaded_at = EXCLUDED.loaded_at
                        """,
                        (fila["id_variable"], fila["fecha"], fila["valor"]),
                    )
            pg_conn.commit()
        
    extraidos = extract_bcra.expand(id_variable=[15, 27, 1, 4, 7])
    load_raw.expand(lista_detalle=extraidos)

bcra_pipeline()