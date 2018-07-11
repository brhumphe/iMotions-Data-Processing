WITH fixations AS
(SELECT DISTINCT
    Name,
    FixationSeq,
    FixationAOI,
    FixationDuration,
    FixationStart
FROM all_raw
WHERE SlideType LIKE '%TestImage%'
AND EventSource LIKE '%ET%'
AND FixationAOI NOT NULL )
SELECT Name, FixationAOI, sum(FixationDuration), min(FixationStart)
FROM fixations
GROUP BY Name, FixationAOI
ORDER BY Name, FixationAOI