import glob
import sqlite3

import pandas as pd

# Create database connection
conn = sqlite3.connect("scarcity_pilot.db")
db = conn.cursor()

# Get file paths of files in ./data/
files = glob.glob("data/Scarcity/*.txt")
print(files)


# Execute a script which will eliminate rows with bad data and insert the
# desired columns into a new table named `data`
def run_sql(sql_file, connection):
    print("Executing ", sql_file)
    fd = open(sql_file, 'r', encoding='utf-8')
    sql_file = fd.read()
    fd.close()
    connection.executescript(sql_file)


# This list of columns is obtained with the code in get_columns.py
selected_columns = [
    # Study and participant data
    # 'StudyName',
    # 'ExportDate',
    'Name',
    'Age',
    'Gender',
    # 'StimuliBlock',
    'StimulusName',
    'SlideType',
    'EventSource',
    'Timestamp',
    # 'MediaTime',
    # 'TimeSignal',

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
    'ValidityLeft',
    'ValidityRight',

    # Eye tracker constructs
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
    'FixationSeq',
    # 'FixationX',
    # 'FixationY',
    'FixationStart',
    'FixationDuration',
    'FixationAOI',

    # PostMarkers are added in iMotions to identify interesting time segments
    'PostMarker',
    # 'Annotation',
    # 'Epoc',
    # 'SDKTimeStamp',

    # ABMBrainState
    'Classification',
    'HighEngagement',
    'LowEngagement',
    'Distraction',
    'Drowsy',
    'WorkloadFBDS',
    'WorkloadBDS',
    'WorkloadAverage',

    # ABMDeconEEG
    # 'Epoc (Decon)',
    # 'Offset (Decon)',
    # 'SDKTimeStamp (Decon)',
    # 'ECG (Decon)',
    # 'POz (Decon)',
    # 'Fz (Decon)',
    # 'Cz (Decon)',
    # 'C3 (Decon)',
    # 'C4 (Decon)',
    # 'F3 (Decon)',
    # 'F4 (Decon)',
    # 'P3 (Decon)',
    # 'P4 (Decon)',

    # ABMRawEEG
    # 'Epoc (Raw)',
    # 'Offset (Raw)',
    # 'SDKTimeStamp (Raw)',
    # 'ECG (Raw)',
    # 'POz (Raw)',
    # 'Fz (Raw)',
    # 'Cz (Raw)',
    # 'C3 (Raw)',
    # 'C4 (Raw)',
    # 'F3 (Raw)',
    # 'F4 (Raw)',
    # 'P3 (Raw)',
    # 'P4 (Raw)',

    # FACET video data
    # 'FrameNo',
    # 'FrameTime',

    # FACET face detection data
    # 'NoOfFaces',  # <-- Only want FACET where one face is visible
    # 'FaceRect X',
    # 'FaceRect Y',
    # 'FaceRect Width',
    # 'FaceRect Height',

    # FACET emotion constructs
    # 'Joy Evidence',
    # 'Joy Intensity',
    # 'Anger Evidence',
    # 'Anger Intensity',
    # 'Surprise Evidence',
    # 'Surprise Intensity',
    # 'Fear Evidence',
    # 'Fear Intensity',
    # 'Contempt Evidence',
    # 'Contempt Intensity',
    # 'Disgust Evidence',
    # 'Disgust Intensity',
    # 'Sadness Evidence',
    # 'Sadness Intensity',
    # 'Confusion Evidence',
    # 'Confusion Intensity',
    # 'Frustration Evidence',
    # 'Frustration Intensity',
    # 'Neutral Evidence',
    # 'Neutral Intensity',
    # 'Positive Evidence',
    # 'Positive Intensity',
    # 'Negative Evidence',
    # 'Negative Intensity',

    # FACET facial action units
    # 'AU1 Evidence', 'AU2 Evidence', 'AU4 Evidence', 'AU5 Evidence',
    # 'AU6 Evidence', 'AU7 Evidence', 'AU9 Evidence', 'AU10 Evidence',
    # 'AU12 Evidence', 'AU14 Evidence', 'AU15 Evidence', 'AU17 Evidence',
    # 'AU18 Evidence', 'AU20 Evidence', 'AU23 Evidence', 'AU24 Evidence',
    # 'AU25 Evidence', 'AU26 Evidence', 'AU28 Evidence', 'AU43 Evidence',

    # FACET raw data on facial features
    # 'Yaw Degrees', 'Pitch Degrees', 'Roll Degrees',
    # 'LEFT_EYE_LATERAL X', 'LEFT_EYE_LATERAL Y',
    # 'LEFT_EYE_PUPIL X', 'LEFT_EYE_PUPIL Y', 'LEFT_EYE_MEDIAL X',
    # 'LEFT_EYE_MEDIAL Y', 'RIGHT_EYE_MEDIAL X',
    # 'RIGHT_EYE_MEDIAL Y', 'RIGHT_EYE_PUPIL X',
    # 'RIGHT_EYE_PUPIL Y', 'RIGHT_EYE_LATERAL X',
    # 'RIGHT_EYE_LATERAL Y', 'NOSE_TIP X', 'NOSE_TIP Y', '7 X',
    # '7 Y',

    # GSR data
    # 'Timestamp RAW (no units) (Shimmer Sensor)',
    # 'Timestamp CAL (mSecs) (Shimmer Sensor)',
    # 'VSenseBatt RAW (no units) (Shimmer Sensor)',
    # 'VSenseBatt CAL (mVolts) (Shimmer Sensor)',
    # 'GSR RAW (no units) (Shimmer Sensor)',
    # 'GSR CAL (kOhms) (Shimmer Sensor)',
    # 'GSR CAL (µSiemens) (Shimmer Sensor)',
    # 'Packet reception rate RAW (no units) (Shimmer Sensor)',
    # 'GSR Quality (Shimmer Sensor)',

    # Because iMotions is stupid, sometimes Shimmer columns are not identical.
    # 'Timestamp RAW (no units) (Shimmer)',
    # 'Timestamp CAL (mSecs) (Shimmer)',
    # 'VSenseBatt RAW (no units) (Shimmer)',
    # 'VSenseBatt CAL (mVolts) (Shimmer)',
    # 'GSR RAW (no units) (Shimmer)',
    # 'GSR CAL (kOhms) (Shimmer)',
    # 'GSR CAL (µSiemens) (Shimmer)',
    # 'Packet reception rate RAW (no units) (Shimmer)',
    # 'GSR Quality (Shimmer)',

    # More iMotions data. Not usually used.
    # 'LiveMarker',
    # 'KeyStroke',
    # 'MarkerText',
    # 'SceneType',
    # 'SceneOutput',
    # 'SceneParent'
    ]

i = 1
total = len(files)
for file in files:
    print(i, '/', total, " : ", file)
    i += 1
    reader = pd.read_csv(file, sep='\t', encoding='utf-8', chunksize=10000,
                         comment='#', skip_blank_lines=True
                         # , usecols=selected_columns
                         )

    # Iterate through file with pandas and write to database. Doing
    # this via pandas is not the most efficient way, though using `usecols=`
    # speeds the process up significantly.
    for chunk in reader:
        # Write raw data to database. Will create the table if it does not
        # already exist
        # chunk = chunk.reindex(columns=selected_columns)
        chunk.to_sql('aoi_data', conn, if_exists='append')
    # run_sql('sql/EEG.sql', connection=conn)

# run_sql('sql/Participants.sql', connection=conn)
