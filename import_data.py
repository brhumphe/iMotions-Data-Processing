import glob
import sqlite3
import time
import pandas as pd
import logging
import sys
import os.path

from utils import read_events, run_sql_file, generate_types

logging.basicConfig(filename="import_data.log",
                    level=logging.DEBUG,
                    format="%(levelname)s|%(asctime)s|%(message)s"
                    )


def process_file(filename, db_name, event_sources,
                 pre_file_sql=None, post_file_sql=None, pre_chunk_sql=None,
                 post_chunk_sql=None, chunksize=100000):
    if pre_chunk_sql is None:
        pre_chunk_sql = []
    if pre_file_sql is None:
        pre_file_sql = []
    if post_chunk_sql is None:
        post_chunk_sql = []
    if post_file_sql is None:
        post_file_sql = []

    with sqlite3.connect(db_name) as connection:
        logging.info('Processing file %s', filename)
        try:
            types = generate_types(filename, event_sources)
            columns = list(types.keys())

            # `usecols` speeds this up significantly. Use it.
            reader = pd.read_csv(filename, sep='\t', encoding='utf-8', chunksize=chunksize, dtype=types,
                                 comment='#', skip_blank_lines=True, usecols=columns)

            for sql in pre_file_sql:
                run_sql_file(sql, connection)

            # Iterate through file with pandas and write to database.
            print("Reading chunks")
            for chunk in reader:
                for sql in pre_chunk_sql:
                    run_sql_file(sql, connection)

                chunk.to_sql('all_raw', connection, if_exists='append')

                for sql in post_chunk_sql:
                    run_sql_file(sql, connection)

            # Run post-processing scripts to filter data
            for sql in post_file_sql:
                run_sql_file(sql, connection)
        except ValueError as e:
            print("Failed to process", filename, file=sys.stderr)
            print(e, file=sys.stderr)
            logging.exception("Failed to process %s\n\t%s", filename, e)


if __name__ == '__main__':
    # This list of columns is obtained with the code in get_columns.py
    # TODO: Replace selected_columns with sensors.py
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

        # PostMarkers are added in iMotions to identify interesting time segments
        'PostMarker',
        # 'Annotation',
        # 'Epoc',
        # 'SDKTimeStamp',

        # ABMBrainState
        # 'Classification',
        # 'HighEngagement',
        # 'LowEngagement',
        # 'Distraction',
        # 'Drowsy',
        # 'WorkloadFBDS',
        # 'WorkloadBDS',
        # 'WorkloadAverage',

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
        'Timestamp RAW (no units) (Shimmer)',
        'Timestamp CAL (mSecs) (Shimmer)',
        'VSenseBatt RAW (no units) (Shimmer)',
        'VSenseBatt CAL (mVolts) (Shimmer)',
        'GSR RAW (no units) (Shimmer)',
        'GSR CAL (kOhms) (Shimmer)',
        'GSR CAL (µSiemens) (Shimmer)',
        'Packet reception rate RAW (no units) (Shimmer)',
        'GSR Quality (Shimmer)',

        # More iMotions data. Not usually used.
        # 'LiveMarker',
        # 'KeyStroke',
        # 'MarkerText',
        # 'SceneType',
        # 'SceneOutput',
        # 'SceneParent'

        # ABM EEG Frontal Asymmetry
        'Delta (1-3 Hz) Asymmetry Log 10 F4/F3 (ABM EEG Frontal Asymmetry)',
        'Delta (1-3 Hz) F3 Average (ABM EEG Frontal Asymmetry)',
        'Delta (1-3 Hz) F4 Average (ABM EEG Frontal Asymmetry)',
        'Theta (4-7 Hz) Asymmetry Log 10 F4/F3 (ABM EEG Frontal Asymmetry)',
        'Theta (4-7 Hz) F3 Average (ABM EEG Frontal Asymmetry)',
        'Theta (4-7 Hz) F4 Average (ABM EEG Frontal Asymmetry)',
        'Alpha (8-12 Hz) Asymmetry Log 10 F4/F3 (ABM EEG Frontal Asymmetry)',
        'Alpha (8-12 Hz) F3 Average (ABM EEG Frontal Asymmetry)',
        'Alpha (8-12 Hz) F4 Average (ABM EEG Frontal Asymmetry)',
        'Beta (13-25 Hz) Asymmetry Log 10 F4/F3 (ABM EEG Frontal Asymmetry)',
        'Beta (13-25 Hz) F3 Average (ABM EEG Frontal Asymmetry)',
        'Beta (13-25 Hz) F4 Average (ABM EEG Frontal Asymmetry)',
        'Gamma (26-40 Hz) Asymmetry Log 10 F4/F3 (ABM EEG Frontal Asymmetry)',
        'Gamma (26-40 Hz) F3 Average (ABM EEG Frontal Asymmetry)',
        'Gamma (26-40 Hz) F4 Average (ABM EEG Frontal Asymmetry)',

        # Performance Metrics Epoc
        # 'Stress (Epoc)',
        # 'Engagement (Epoc)',
        # 'Relaxation (Epoc)',
        # 'Excitement (Epoc)',
        # 'Interest (Epoc)'

    ]
    logging.debug("Using columns: %s", selected_columns)

    start = time.time()
    # print('Began at', start)
    # Create database connection
    db_file = "psd_data.db"

    files = glob.glob(r"F:\adidas\sensor data\Experience*sensor data*\**low*\*_*.txt")
    # files = [r"F:\adidas\sensor data\Experience all video sensor data\low session 2 - POST\001_L103.txt"]
    total = len(files)
    logging.info("Processing files: %s", files)
    for i, file in enumerate(files, start=1):
        print(f"Processing file {i}/{total} {file}")
        logging.info(f"Processing {file}")

        db_name = file + ".db"
        if not os.path.isfile(db_name):
            process_file(file, db_name, ['ABM EEG Frontal Asymmetry'],
                         pre_file_sql=["sql/db_setup_psd_shimmer.sql"],
                         post_file_sql=["sql/psd_shimmer_sensor.sql", "sql/cleanup.sql"]
                         )
        else:
            print(f"File exists: {db_name}", file=sys.stderr)
            logging.exception(f"File exists: {db_name}")

    end = time.time()
    print('Total time:', (end - start) / 60, 'minutes')

# sample_filename =  r"F:\adidas\sensor data\WMC sensor data\low session 2 - POST\010_L106-2.txt"
