SELECT
    p.Name
    , p.Age
    , p.Gender
    , p.Condition
    , pm.PostMarker
    , avg(Classification)
    , avg(HighEngagement)
    , avg(LowEngagement)
    , avg(Distraction)
    , avg(Drowsy)
    , avg(WorkloadFBDS)
    , avg(WorkloadBDS)
    , avg(WorkloadAverage)
FROM PostMarkers pm
    JOIN eeg e
        ON pm."index" = e."index"
    JOIN Participants p
        ON e.Name = p.Name
WHERE p.Condition = pm.Condition

GROUP BY p.Condition, p.Name, pm.PostMarker
ORDER BY e.Name, e.PostMarker