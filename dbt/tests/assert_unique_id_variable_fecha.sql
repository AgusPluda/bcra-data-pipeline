SELECT
    id_variable,
    fecha
FROM {{ ref('fct_bcra_series_daily') }}
GROUP BY id_variable, fecha
HAVING COUNT(*) > 1