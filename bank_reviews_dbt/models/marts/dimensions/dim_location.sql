SELECT

    id AS location_id,

    bank_url,

    address,

    city,

    latitude,

    longitude

FROM {{ ref('stg_banks') }}