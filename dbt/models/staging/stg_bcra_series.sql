SELECT
    id_variable,
    fecha,
    CAST(valor AS NUMERIC) AS cifra,
    loaded_at AS cargado_en
FROM {{ source('raw', 'bcra_series') }}