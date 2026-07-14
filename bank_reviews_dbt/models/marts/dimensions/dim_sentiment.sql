WITH distinct_sentiments AS (

    SELECT DISTINCT
        sentiment

    FROM {{ ref('stg_reviews') }}

    WHERE sentiment IS NOT NULL

)

SELECT

    ROW_NUMBER() OVER (ORDER BY sentiment) AS sentiment_id,

    sentiment

FROM distinct_sentiments