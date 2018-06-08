SELECT
  Name,
  Age,
  Gender,
  PostMarker,
--   Timestamp,
  Timestamp / 1000 AS "Timestamp",
  avg(Classification)  AS "Classification",
  avg(HighEngagement)  AS "HighEngagement",
  avg(LowEngagement)   AS "LowEngagement",
  avg(Distraction)     AS "Distraction",
  avg(Drowsy)          AS "Drowsy",
  avg(WorkloadFBDS)    AS "WorkloadFBDS",
  avg(WorkloadBDS)     AS "WorkloadBDS",
  avg(WorkloadAverage) AS "WorkloadAverage"
FROM eeg
GROUP BY (Timestamp / 1000)