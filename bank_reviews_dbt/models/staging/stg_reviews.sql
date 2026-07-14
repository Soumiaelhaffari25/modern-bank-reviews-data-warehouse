SELECT

    review_id,
    bank_url,
    author,
    rating,
    review_date,
    review_text,
    language,
    sentiment,
    topic,
    keywords,
    scraped_at

FROM {{ source('bank_reviews', 'reviews') }}