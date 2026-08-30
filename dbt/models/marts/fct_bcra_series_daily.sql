SELECT
    s.id_variable,
    s.fecha,
    d.descripcion,
    d.periodicidad,
    d.unidad,
    s.cifra,
    s.cargado_en
FROM {{ ref('stg_bcra_series') }} AS s
LEFT JOIN {{ ref('dim_bcra_variable') }} AS d ON d.id_variable = s.id_variable