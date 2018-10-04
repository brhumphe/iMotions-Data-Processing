import numpy as np

STUDY_INFO = {
    'StudyName': str,
    'ExportDate': str,
    'Name': str,
    'Age': int,
    'Gender': str,
    # 'StimuliBlock': str,
    'StimulusName': str,
    'SlideType': str,
    'EventSource': str,
    'Timestamp': str,
    'PostMarker': str
}

ABMBrainState = {
    'Classification': np.float64,
    'HighEngagement': np.float64,
    'LowEngagement': np.float64,
    'Distraction': np.float64,
    'Drowsy': np.float64,
    'WorkloadFBDS': np.float64,
    'WorkloadBDS': np.float64,
    'WorkloadAverage': np.float64
}

ABM_Frontal_Asymmetry = {
    'Delta (1-3 Hz) Asymmetry Log 10 F4/F3 (ABM EEG Frontal Asymmetry)': np.float64,
    'Delta (1-3 Hz) F3 Average (ABM EEG Frontal Asymmetry)': np.float64,
    'Delta (1-3 Hz) F4 Average (ABM EEG Frontal Asymmetry)': np.float64,
    'Theta (4-7 Hz) Asymmetry Log 10 F4/F3 (ABM EEG Frontal Asymmetry)': np.float64,
    'Theta (4-7 Hz) F3 Average (ABM EEG Frontal Asymmetry)': np.float64,
    'Theta (4-7 Hz) F4 Average (ABM EEG Frontal Asymmetry)': np.float64,
    'Alpha (8-12 Hz) Asymmetry Log 10 F4/F3 (ABM EEG Frontal Asymmetry)': np.float64,
    'Alpha (8-12 Hz) F3 Average (ABM EEG Frontal Asymmetry)': np.float64,
    'Alpha (8-12 Hz) F4 Average (ABM EEG Frontal Asymmetry)': np.float64,
    'Beta (13-25 Hz) Asymmetry Log 10 F4/F3 (ABM EEG Frontal Asymmetry)': np.float64,
    'Beta (13-25 Hz) F3 Average (ABM EEG Frontal Asymmetry)': np.float64,
    'Beta (13-25 Hz) F4 Average (ABM EEG Frontal Asymmetry)': np.float64,
    'Gamma (26-40 Hz) Asymmetry Log 10 F4/F3 (ABM EEG Frontal Asymmetry)': np.float64,
    'Gamma (26-40 Hz) F3 Average (ABM EEG Frontal Asymmetry)': np.float64,
    'Gamma (26-40 Hz) F4 Average (ABM EEG Frontal Asymmetry)': np.float64
}

Shimmer = {
    # 'Timestamp RAW (no units) (Shimmer)': np.float64,
    # 'Timestamp CAL (mSecs) (Shimmer)': np.float64,
    # 'VSenseBatt RAW (no units) (Shimmer)': np.float64,
    # 'VSenseBatt CAL (mVolts) (Shimmer)': np.float64,
    'GSR RAW (no units) (Shimmer)': np.float64,
    'GSR CAL (kOhms) (Shimmer)': np.float64,
    'GSR CAL (µSiemens) (Shimmer)': np.float64,
    # 'Packet reception rate RAW (no units) (Shimmer)': np.float64,
    'GSR Quality (Shimmer)': str
}

Shimmer_Sensor = {
    # 'Timestamp RAW (no units) (Shimmer Sensor)': np.float64,
    # 'Timestamp CAL (mSecs) (Shimmer Sensor)': np.float64,
    # 'VSenseBatt RAW (no units) (Shimmer Sensor)': np.float64,
    # 'VSenseBatt CAL (mVolts) (Shimmer Sensor)': np.float64,
    'GSR RAW (no units) (Shimmer Sensor)': np.float64,
    'GSR CAL (kOhms) (Shimmer Sensor)': np.float64,
    'GSR CAL (µSiemens) (Shimmer Sensor)': np.float64,
    # 'Packet reception rate RAW (no units) (Shimmer Sensor)': np.float64,
    'GSR Quality (Shimmer Sensor)': str
}

Emotient_FACET = {
    'Joy Evidence': np.float64,
    # 'Joy Intensity': np.float64,
    'Anger Evidence': np.float64,
    # 'Anger Intensity': np.float64,
    'Surprise Evidence': np.float64,
    # 'Surprise Intensity': np.float64,
    'Fear Evidence': np.float64,
    # 'Fear Intensity': np.float64,
    'Contempt Evidence': np.float64,
    # 'Contempt Intensity': np.float64,
    'Disgust Evidence': np.float64,
    # 'Disgust Intensity': np.float64,
    'Sadness Evidence': np.float64,
    # 'Sadness Intensity': np.float64,
    'Confusion Evidence': np.float64,
    # 'Confusion Intensity': np.float64,
    'Frustration Evidence': np.float64,
    # 'Frustration Intensity': np.float64,
    'Neutral Evidence': np.float64,
    # 'Neutral Intensity': np.float64,
    'Positive Evidence': np.float64,
    # 'Positive Intensity': np.float64,
    'Negative Evidence': np.float64,
    # 'Negative Intensity': np.float64
}