import glob
import sqlite3
import time
import pandas as pd
import logging

logging.basicConfig(filename="import_data.log",
                    level=logging.DEBUG
                    # ,
                    # format="%(asctime)s:%(levelname)s:%(message)s"
                    )

# files = glob.glob("D:\\Adidas 1.1\\adidas 1.11\\ToL/*.txt")
# files = glob.glob("D:\\Adidas 1.1\\02_A_adidas 1.11 ToL/*.txt")
files = glob.glob("D:\\Adidas 1.1\\adidas 1.11\\WMC/*.txt")
logging.debug("Files: %s", files)

# Create database connection
# conn = sqlite3.connect(":memory:")
database = "WMC.db"
conn = sqlite3.connect(database)
db = conn.cursor()
logging.debug("Connected to %s", database)


def run_sql(sql_file, connection):
    print("Executing ", sql_file)
    logging.debug("Executing %s", sql_file)
    try:
        fd = open(sql_file, 'r', encoding='utf-8')
        sql_file = fd.read()
        fd.close()
        connection.executescript(sql_file)
    except:
        logging.exception("Failed to run %s", sql_file)


# This list of columns is obtained with the code in get_columns.py
selected_columns = [
    # Study and participant data
    'StudyName',
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
    # 'ValidityLeft',
    # 'ValidityRight',

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
    # 'FixationSeq',
    # 'FixationX',
    # 'FixationY',
    # 'FixationStart',
    # 'FixationDuration',
    # 'FixationAOI',

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
logging.debug("Using columns: %s", selected_columns)

start = time.time()
print('Began at', start)
total = len(files)
for i, file in enumerate(files):
    print(i + 1, '/', total, " : ", file)
    logging.info("Processing %s", file)

    try:
        reader = pd.read_csv(file, sep='\t', encoding='utf-8', chunksize=100000,
                             comment='#', skip_blank_lines=True
                             , usecols=selected_columns
                             )

        # Iterate through file with pandas and write to database. Doing
        # this via pandas is not the most efficient way, though using `usecols=`
        # speeds the process up significantly.
        for _, chunk in enumerate(reader):
            # Write raw data to database. Will create the table if it does not
            # already exist
            # chunk = chunk.reindex(columns=selected_columns)
            # print('Processing chunk', i + 1, 'from ', file)
            chunk.to_sql('all_raw', conn, if_exists='append')
        run_sql('sql/EEG.sql', connection=conn)
    except ValueError as e:
        print("Failed to process", file)
        logging.exception("Failed to process %s", file)

run_sql('sql/Participants.sql', connection=conn)
end = time.time()
print('Total time:', (end - start) / 60, 'minutes')
