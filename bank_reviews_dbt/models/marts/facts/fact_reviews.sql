SELECT

    r.review_id,

    b.bank_id,

    l.location_id,

    s.sentiment_id,

    t.topic_id,

    r.author,

    r.rating,

    r.review_date,

    r.review_text,

    r.language,

    r.keywords,

    r.scraped_at

FROM {{ ref('stg_reviews') }} r

JOIN {{ ref('dim_bank') }} b
    ON r.bank_url = b.bank_url

JOIN {{ ref('stg_banks') }} sb
    ON r.bank_url = sb.bank_url

JOIN {{ ref('dim_location') }} l
    ON sb.bank_url = l.bank_url

LEFT JOIN {{ ref('dim_sentiment') }} s
    ON r.sentiment = s.sentiment

LEFT JOIN {{ ref('dim_topic') }} t
    ON r.topic = t.topic