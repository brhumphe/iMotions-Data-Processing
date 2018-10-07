INSERT INTO clean
SELECT
    "index",
    StudyName,
    Name,
    Age,
    Gender,
    StimulusName,
    SlideType,
    EventSource,
    Timestamp,
    PostMarker,
--     "Timestamp RAW (no units) (Shimmer Sensor)",
--     "Timestamp CAL (mSecs) (Shimmer Sensor)",
--     "VSenseBatt RAW (no units) (Shimmer Sensor)",
--     "VSenseBatt CAL (mVolts) (Shimmer Sensor)",
--     "GSR RAW (no units) (Shimmer Sensor)",
--     "GSR CAL (kOhms) (Shimmer Sensor)",
--     "GSR CAL (µSiemens) (Shimmer Sensor)",
--     "Packet reception rate RAW (no units) (Shimmer Sensor)",
--     "GSR Quality (Shimmer Sensor)",
    "Timestamp RAW (no units) (Shimmer)",
    "Timestamp CAL (mSecs) (Shimmer)",
    "VSenseBatt RAW (no units) (Shimmer)",
    "VSenseBatt CAL (mVolts) (Shimmer)",
    "GSR RAW (no units) (Shimmer)",
    "GSR CAL (kOhms) (Shimmer)",
    "GSR CAL (µSiemens) (Shimmer)",
    "Packet reception rate RAW (no units) (Shimmer)",
    "GSR Quality (Shimmer)",
    "Delta (1-3 Hz) Asymmetry Log 10 F4/F3 (ABM EEG Frontal Asymmetry)",
    "Delta (1-3 Hz) F3 Average (ABM EEG Frontal Asymmetry)",
    "Delta (1-3 Hz) F4 Average (ABM EEG Frontal Asymmetry)",
    "Theta (4-7 Hz) Asymmetry Log 10 F4/F3 (ABM EEG Frontal Asymmetry)",
    "Theta (4-7 Hz) F3 Average (ABM EEG Frontal Asymmetry)",
    "Theta (4-7 Hz) F4 Average (ABM EEG Frontal Asymmetry)",
    "Alpha (8-12 Hz) Asymmetry Log 10 F4/F3 (ABM EEG Frontal Asymmetry)",
    "Alpha (8-12 Hz) F3 Average (ABM EEG Frontal Asymmetry)",
    "Alpha (8-12 Hz) F4 Average (ABM EEG Frontal Asymmetry)",
    "Beta (13-25 Hz) Asymmetry Log 10 F4/F3 (ABM EEG Frontal Asymmetry)",
    "Beta (13-25 Hz) F3 Average (ABM EEG Frontal Asymmetry)",
    "Beta (13-25 Hz) F4 Average (ABM EEG Frontal Asymmetry)",
    "Gamma (26-40 Hz) Asymmetry Log 10 F4/F3 (ABM EEG Frontal Asymmetry)",
    "Gamma (26-40 Hz) F3 Average (ABM EEG Frontal Asymmetry)",
    "Gamma (26-40 Hz) F4 Average (ABM EEG Frontal Asymmetry)"
FROM
    all_raw
WHERE
--     "GSR Quality (Shimmer Sensor)" LIKE 'VALID'
    "GSR Quality (Shimmer)" NOT LIKE 'INVALID'
    AND
    SlideType NOT LIKE 'BlackInterslide'
    AND
    (EventSource LIKE '%Shimmer%' OR EventSource LIKE '%ABM EEG Frontal Asymmetry%')