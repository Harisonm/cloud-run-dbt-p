{{ config(
    materialized='view',
    schema="ds_edw",
    table="lookerstudio_report"
    ) }}

SELECT * 
FROM {{ ref('lookerstudio_report') }}
WHERE Year in (2022)