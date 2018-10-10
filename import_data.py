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

            # TODO: Don't create a database unless there is valid data to add to it
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
    start = time.time()
    # print('Began at', start)
    # Create database connection
    db_file = "psd_data.db"

    files = glob.glob(r"F:\adidas\sensor data\Experience all video sensor data\low session 1 - PRE\psd+shimmer\*_*.txt")
    # files = [r"F:\adidas\sensor data\Experience all video sensor data\low session 2 - POST\001_L103.txt"]
    total = len(files)
    logging.info("Processing files: %s", files)
    for i, file in enumerate(files, start=1):
        print(f"Processing file {i}/{total} {file}")
        logging.info(f"Processing {file}")

        db_name = os.path.splitext(file)[0] + ".db"
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
