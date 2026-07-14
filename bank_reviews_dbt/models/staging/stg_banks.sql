SELECT

    id,
    bank_name,
    url AS bank_url,
    address,
    city,
    latitude,
    longitude,
    scraped_at

FROM {{ source('bank_reviews', 'banks') }}