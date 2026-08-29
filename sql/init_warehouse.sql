-- Inicializa la warehouse database
CREATE SCHEMA raw;

CREATE TABLE raw.bcra_series (
    id_variable INT,
    fecha DATE,
    valor NUMERIC, 
    loaded_at TIMESTAMPTZ DEFAULT now(),
    PRIMARY KEY (id_variable, fecha)
);
-- Notas: 
    -- fecha: DATE en vez de TEXT, no respeta de todo el proceso "raw" del pipeline pero esto mismo ayudaria
    --        a poder detectar al instante fechas inconsistentes de ingresos de datos (ej. fechas pasadas).
    -- valor: NUMERIC en vez de FLOAT para obtener los valores exactos.