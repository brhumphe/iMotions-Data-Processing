--DROP TABLE IF EXISTS eeg;
CREATE TABLE IF NOT EXISTS eeg (
    "index"         INTEGER,
    Name            INTEGER,
    Age             INTEGER,
    Gender          TEXT,
    Timestamp       TEXT,
    PostMarker      TEXT,
    Classification  NUMERIC,
    HighEngagement  FLOAT,
    LowEngagement   FLOAT,
    Distraction     FLOAT,
    Drowsy          FLOAT,
    WorkloadFBDS    FLOAT,
    WorkloadBDS     FLOAT,
    WorkloadAverage FLOAT
);


INSERT INTO eeg
    SELECT
        "index",
        Name,
        Age,
        Gender,
        Timestamp,
        PostMarker,
        Classification,
        HighEngagement,
        LowEngagement,
        Distraction,
        Drowsy,
        WorkloadFBDS,
        WorkloadBDS,
        WorkloadAverage
    FROM all_raw
    WHERE
        EventSource LIKE '%ABMBrainState%' AND Classification != -1 AND HighEngagement != -1 AND LowEngagement != -1 AND
        Distraction != -1 AND Drowsy != -1 AND WorkloadFBDS != -1 AND WorkloadBDS != -1 AND WorkloadAverage != -1
        AND SlideType LIKE 'TestImage';

-- Delete raw data and purge it from the database with VACUUM
--DELETE FROM all_raw;
--VACUUM;