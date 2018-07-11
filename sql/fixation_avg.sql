WITH fixations AS (SELECT DISTINCT
                       lower(Name) AS Name
                       , FixationAOI
                       , FixationStart
                       , FixationDuration
                       , FixationSeq
                   FROM all_raw
                   WHERE
                       SlideType LIKE 'TestImage'
                       AND FixationAOI NOTNULL )
SELECT
    Name
    , FixationAOI
    , min(FixationStart) AS FixationStart
    , sum(FixationDuration)
FROM fixations
GROUP BY Name, FixationAOI
ORDER BY Name, FixationAOI