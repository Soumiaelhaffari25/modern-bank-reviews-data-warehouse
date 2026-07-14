SELECT DISTINCT

    id AS bank_id,
    bank_name,
    bank_url

FROM {{ ref('stg_banks') }}