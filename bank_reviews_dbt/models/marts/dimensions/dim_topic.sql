WITH distinct_topics AS (

    SELECT DISTINCT
        topic

    FROM {{ ref('stg_reviews') }}

    WHERE topic IS NOT NULL

)

SELECT

    ROW_NUMBER() OVER (ORDER BY topic) AS topic_id,

    topic

FROM distinct_topics