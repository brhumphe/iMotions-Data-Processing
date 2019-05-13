import numpy as np


STUDY_INFO = {
    'StudyName': str,
    # 'ExportDate': str,
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

ET = {
    'ValidityLeft': np.float,
    'ValidityRight': np.float,
    'PupilLeft': np.float,
    'PupilRight': np.float,
    'FixationX': np.float,
    'FixationY': np.float,
    'FixationAOI': str,
    'FixationStart': np.float,  # Double check this
    'FixationDuration': np.float,
    'FixationSeq': np.float,
    'AccX': np.float,
    'AccY': np.float,
    'AccZ': np.float,
    'GyroX': np.float,
    'GyroY': np.float,
    'GyroZ': np.float,
    'Gaze3DX': np.float,
    'Gaze3DY': np.float,
    'Gaze3DZ': np.float,
    'Distance3D': np.float,
    'GazeDirectionLeftX': np.float,
    'GazeDirectionLeftY': np.float,
    'GazeDirectionLeftZ': np.float,
    'GazeDirectionRightX': np.float,
    'GazeDirectionRightY': np.float,
    'GazeDirectionRightZ': np.float,
    'GazeX': np.float,
    'GazeY': np.float,
    'GazeAOI': np.float,
    'InterpolatedGazeX': np.float,
    'InterpolatedGazeY': np.float,
    'GazeEventType': np.float,
    'GazeVelocityAngle': np.float,
    'SaccadeSeq': np.float,
    'SaccadeStart': np.float,
    'SaccadeDuration': np.float,
}

Epoc_Performance_Metrics = {
    # Performance Metrics Epoc
    'Stress (Epoc)': np.float64,
    'Engagement (Epoc)': np.float64,
    'Relaxation (Epoc)': np.float64,
    'Excitement (Epoc)': np.float64,
    'Interest (Epoc)': np.float64
}

Performance_Metrics_Emotiv_Cortex = {
    'Interest (Emotiv Cortex)': np.float64,
    'Stress (Emotiv Cortex)': np.float64,
    'Relaxation (Emotiv Cortex)': np.float64,
    'Excitement (Emotiv Cortex)': np.float64,
    'Engagement (Emotiv Cortex)': np.float64,
    'Long term excitement (Emotiv Cortex)': np.float64,
    'Focus (Emotiv Cortex)': np.float64
}

Motion_Emotiv_Cortex = {
    'GYROX (Emotiv Cortex)': np.float64,
    'GYROY (Emotiv Cortex)': np.float64,
    'GYROZ (Emotiv Cortex)': np.float64,
    'ACCX (Emotiv Cortex)': np.float64,
    'ACCY (Emotiv Cortex)': np.float64,
    'ACCZ (Emotiv Cortex)': np.float64,
    'MAGX (Emotiv Cortex)': np.float64,
    'MAGY (Emotiv Cortex)': np.float64,
    'MAGZ (Emotiv Cortex)': np.float64
}

Affdex_Raw = {
    'Number of faces': np.float64,
    # 'width': np.float64,
    # 'height': np.float64,
    # 'FrameIndex': np.float64,
    # 'faceid': np.float64,
    # '#classifiers': np.float64,
    # 'Brow Furrow': np.float64,
    # 'Brow Raise': np.float64,
    'Engagement': np.float64,
    # 'Lip Corner Depressor': np.float64,
    'Smile': np.float64,
    'Valence': np.float64,
    'Attention': np.float64,
    # 'Interocular Distance': np.float64,
    # 'Pitch': np.float64,
    # 'Yaw': np.float64,
    # 'Roll': np.float64,
    # 'InnerBrowRaise': np.float64,
    # 'EyeClosure': np.float64,
    # 'NoseWrinkle': np.float64,
    # 'UpperLipRaise': np.float64,
    # 'LipSuck': np.float64,
    # 'LipPress': np.float64,
    # 'MouthOpen': np.float64,
    # 'ChinRaise': np.float64,
    # 'Smirk': np.float64,
    # 'LipPucker': np.float64,
    'Anger': np.float64,
    'Sadness': np.float64,
    'Disgust': np.float64,
    'Joy': np.float64,
    'Surprise': np.float64,
    'Fear': np.float64,
}

EventNames = {
    'ABMBrainState': ABMBrainState,
    'ABM EEG Frontal Asymmetry': ABM_Frontal_Asymmetry,
    'Shimmer': Shimmer,
    'Shimmer Sensor': Shimmer_Sensor,
    'Shimmer Sensor Shimmer Sensor': Shimmer_Sensor,
    'ET': ET,
    'Performance Metrics Epoc': Epoc_Performance_Metrics,
    'Performance Metrics Emotiv Cortex': Performance_Metrics_Emotiv_Cortex,
    'Motion Emotiv Cortex': Motion_Emotiv_Cortex,
    'AffRaw': Affdex_Raw
}

# selected_columns = [
#     # Study and participant data
#     'StudyName',
#     # 'ExportDate',
#     'Name',
#     'Age',
#     'Gender',
#     # 'StimuliBlock',
#     'StimulusName',
#     'SlideType',
#     'EventSource',
#     'Timestamp',
#     # 'MediaTime',
#     # 'TimeSignal',
#
#     # Eye tracker raw data
#     # 'GazeLeftx',
#     # 'GazeLefty',
#     # 'GazeRightx',
#     # 'GazeRighty',
#
#     # Eye tracker Pupil Dilation
#     # 'PupilLeft',
#     # 'PupilRight',
#
#     # Eye tracker raw data
#     # 'DistanceLeft',
#     # 'DistanceRight',
#     # 'CameraLeftX',
#     # 'CameraLeftY',
#     # 'CameraRightX',
#     # 'CameraRightY',
#
#     # Whether the eye is being tracked. 0 if data is valid.
#     # ET Validity
#     # 'ValidityLeft',
#     # 'ValidityRight',
#
#     # Eye tracker
#     # 'GazeX',
#     # 'GazeY',
#     # 'GazeAOI',
#     # 'InterpolatedGazeX',
#     # 'InterpolatedGazeY',
#     # 'GazeEventType',
#     # 'GazeVelocityAngle',
#     # 'SaccadeSeq',
#     # 'SaccadeStart',
#     # 'SaccadeDuration',
#
#     # ET Fixations
#     # 'FixationSeq',
#     # 'FixationX',
#     # 'FixationY',
#     # 'FixationStart',
#     # 'FixationDuration',
#     # 'FixationAOI',
#
#     # PostMarkers are added in iMotions to identify interesting time segments
#     'PostMarker',
#     # 'Annotation',
#     # 'Epoc',
#     # 'SDKTimeStamp',
#
#     # ABMBrainState
#     # 'Classification',
#     # 'HighEngagement',
#     # 'LowEngagement',
#     # 'Distraction',
#     # 'Drowsy',
#     # 'WorkloadFBDS',
#     # 'WorkloadBDS',
#     # 'WorkloadAverage',
#
#     # ABMDeconEEG
#     # 'Epoc (Decon)',
#     # 'Offset (Decon)',
#     # 'SDKTimeStamp (Decon)',
#     # 'ECG (Decon)',
#     # 'POz (Decon)',
#     # 'Fz (Decon)',
#     # 'Cz (Decon)',
#     # 'C3 (Decon)',
#     # 'C4 (Decon)',
#     # 'F3 (Decon)',
#     # 'F4 (Decon)',
#     # 'P3 (Decon)',
#     # 'P4 (Decon)',
#
#     # ABMRawEEG
#     # 'Epoc (Raw)',
#     # 'Offset (Raw)',
#     # 'SDKTimeStamp (Raw)',
#     # 'ECG (Raw)',
#     # 'POz (Raw)',
#     # 'Fz (Raw)',
#     # 'Cz (Raw)',
#     # 'C3 (Raw)',
#     # 'C4 (Raw)',
#     # 'F3 (Raw)',
#     # 'F4 (Raw)',
#     # 'P3 (Raw)',
#     # 'P4 (Raw)',
#
#     # FACET video data
#     # 'FrameNo',
#     # 'FrameTime',
#
#     # FACET face detection data
#     # 'NoOfFaces',  # <-- Only want FACET where one face is visible
#     # 'FaceRect X',
#     # 'FaceRect Y',
#     # 'FaceRect Width',
#     # 'FaceRect Height',
#
#     # FACET emotion constructs
#     # 'Joy Evidence',
#     # 'Joy Intensity',
#     # 'Anger Evidence',
#     # 'Anger Intensity',
#     # 'Surprise Evidence',
#     # 'Surprise Intensity',
#     # 'Fear Evidence',
#     # 'Fear Intensity',
#     # 'Contempt Evidence',
#     # 'Contempt Intensity',
#     # 'Disgust Evidence',
#     # 'Disgust Intensity',
#     # 'Sadness Evidence',
#     # 'Sadness Intensity',
#     # 'Confusion Evidence',
#     # 'Confusion Intensity',
#     # 'Frustration Evidence',
#     # 'Frustration Intensity',
#     # 'Neutral Evidence',
#     # 'Neutral Intensity',
#     # 'Positive Evidence',
#     # 'Positive Intensity',
#     # 'Negative Evidence',
#     # 'Negative Intensity',
#
#     # FACET facial action units
#     # 'AU1 Evidence', 'AU2 Evidence', 'AU4 Evidence', 'AU5 Evidence',
#     # 'AU6 Evidence', 'AU7 Evidence', 'AU9 Evidence', 'AU10 Evidence',
#     # 'AU12 Evidence', 'AU14 Evidence', 'AU15 Evidence', 'AU17 Evidence',
#     # 'AU18 Evidence', 'AU20 Evidence', 'AU23 Evidence', 'AU24 Evidence',
#     # 'AU25 Evidence', 'AU26 Evidence', 'AU28 Evidence', 'AU43 Evidence',
#
#     # FACET raw data on facial features
#     # 'Yaw Degrees', 'Pitch Degrees', 'Roll Degrees',
#     # 'LEFT_EYE_LATERAL X', 'LEFT_EYE_LATERAL Y',
#     # 'LEFT_EYE_PUPIL X', 'LEFT_EYE_PUPIL Y', 'LEFT_EYE_MEDIAL X',
#     # 'LEFT_EYE_MEDIAL Y', 'RIGHT_EYE_MEDIAL X',
#     # 'RIGHT_EYE_MEDIAL Y', 'RIGHT_EYE_PUPIL X',
#     # 'RIGHT_EYE_PUPIL Y', 'RIGHT_EYE_LATERAL X',
#     # 'RIGHT_EYE_LATERAL Y', 'NOSE_TIP X', 'NOSE_TIP Y', '7 X',
#     # '7 Y',
#
#     # GSR data
#     # 'Timestamp RAW (no units) (Shimmer Sensor)',
#     # 'Timestamp CAL (mSecs) (Shimmer Sensor)',
#     # 'VSenseBatt RAW (no units) (Shimmer Sensor)',
#     # 'VSenseBatt CAL (mVolts) (Shimmer Sensor)',
#     # 'GSR RAW (no units) (Shimmer Sensor)',
#     # 'GSR CAL (kOhms) (Shimmer Sensor)',
#     # 'GSR CAL (µSiemens) (Shimmer Sensor)',
#     # 'Packet reception rate RAW (no units) (Shimmer Sensor)',
#     # 'GSR Quality (Shimmer Sensor)',
#
#     # Because iMotions is stupid, sometimes Shimmer columns are not identical.
#     'Timestamp RAW (no units) (Shimmer)',
#     'Timestamp CAL (mSecs) (Shimmer)',
#     'VSenseBatt RAW (no units) (Shimmer)',
#     'VSenseBatt CAL (mVolts) (Shimmer)',
#     'GSR RAW (no units) (Shimmer)',
#     'GSR CAL (kOhms) (Shimmer)',
#     'GSR CAL (µSiemens) (Shimmer)',
#     'Packet reception rate RAW (no units) (Shimmer)',
#     'GSR Quality (Shimmer)',
#
#     # More iMotions data. Not usually used.
#     # 'LiveMarker',
#     # 'KeyStroke',
#     # 'MarkerText',
#     # 'SceneType',
#     # 'SceneOutput',
#     # 'SceneParent'
#
#     # ABM EEG Frontal Asymmetry
#     'Delta (1-3 Hz) Asymmetry Log 10 F4/F3 (ABM EEG Frontal Asymmetry)',
#     'Delta (1-3 Hz) F3 Average (ABM EEG Frontal Asymmetry)',
#     'Delta (1-3 Hz) F4 Average (ABM EEG Frontal Asymmetry)',
#     'Theta (4-7 Hz) Asymmetry Log 10 F4/F3 (ABM EEG Frontal Asymmetry)',
#     'Theta (4-7 Hz) F3 Average (ABM EEG Frontal Asymmetry)',
#     'Theta (4-7 Hz) F4 Average (ABM EEG Frontal Asymmetry)',
#     'Alpha (8-12 Hz) Asymmetry Log 10 F4/F3 (ABM EEG Frontal Asymmetry)',
#     'Alpha (8-12 Hz) F3 Average (ABM EEG Frontal Asymmetry)',
#     'Alpha (8-12 Hz) F4 Average (ABM EEG Frontal Asymmetry)',
#     'Beta (13-25 Hz) Asymmetry Log 10 F4/F3 (ABM EEG Frontal Asymmetry)',
#     'Beta (13-25 Hz) F3 Average (ABM EEG Frontal Asymmetry)',
#     'Beta (13-25 Hz) F4 Average (ABM EEG Frontal Asymmetry)',
#     'Gamma (26-40 Hz) Asymmetry Log 10 F4/F3 (ABM EEG Frontal Asymmetry)',
#     'Gamma (26-40 Hz) F3 Average (ABM EEG Frontal Asymmetry)',
#     'Gamma (26-40 Hz) F4 Average (ABM EEG Frontal Asymmetry)',
#
#     # Performance Metrics Epoc
#     # 'Stress (Epoc)',
#     # 'Engagement (Epoc)',
#     # 'Relaxation (Epoc)',
#     # 'Excitement (Epoc)',
#     # 'Interest (Epoc)'
#
# ]

# Eye tracker raw data
# 'GazeLeftx',
# 'GazeLefty',
# 'GazeRightx',
# 'GazeRighty',

# Eye tracker Pupil Dilation
# 'PupilLeft',
# 'PupilRight',

# Eye tracker raw data
# 'DistanceLeft',
# 'DistanceRight',
# 'CameraLeftX',
# 'CameraLeftY',
# 'CameraRightX',
# 'CameraRightY',

# Whether the eye is being tracked. 0 if data is valid.
# ET Validity
# 'ValidityLeft',
# 'ValidityRight',

# Eye tracker
# 'GazeX',
# 'GazeY',
# 'GazeAOI',
# 'InterpolatedGazeX',
# 'InterpolatedGazeY',
# 'GazeEventType',
# 'GazeVelocityAngle',
# 'SaccadeSeq',
# 'SaccadeStart',
# 'SaccadeDuration',

# ET Fixations
# 'FixationSeq',
# 'FixationX',
# 'FixationY',
# 'FixationStart',
# 'FixationDuration',
# 'FixationAOI',
