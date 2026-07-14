SELECT

    f.review_id,

    b.bank_name,

    l.address,

    l.city,

    l.latitude,

    l.longitude,

    s.sentiment,

    t.topic,

    f.author,

    f.rating,

    f.review_date,

    f.review_text,

    f.language,

    f.keywords,

    f.scraped_at

FROM {{ ref('fact_reviews') }} f

LEFT JOIN {{ ref('dim_bank') }} b
    ON f.bank_id = b.bank_id

LEFT JOIN {{ ref('dim_location') }} l
    ON f.location_id = l.location_id

LEFT JOIN {{ ref('dim_sentiment') }} s
    ON f.sentiment_id = s.sentiment_id

LEFT JOIN {{ ref('dim_topic') }} t
    ON f.topic_id = t.topic_id