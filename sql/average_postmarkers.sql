SELECT
  Name,
  Age,
  Gender,
  PostMarker,
  avg(Classification)  AS "Classification",
  avg(HighEngagement)  AS "HighEngagement",
  avg(LowEngagement)   AS "LowEngagement",
  avg(Distraction)     AS "Distraction",
  avg(Drowsy)          AS "Drowsy",
  avg(WorkloadFBDS)    AS "WorkloadFBDS",
  avg(WorkloadBDS)     AS "WorkloadBDS",
  avg(WorkloadAverage) AS "WorkloadAverage"
FROM abm_eeg
WHERE
  PostMarker NOT NULL
GROUP BY Name, Age, Gender, PostMarker
ORDER BY Name