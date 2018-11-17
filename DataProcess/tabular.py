import csv
import glob
import os
from itertools import dropwhile
import dataset


def skip_comments(path, prefix='#'):
    """
Opens file at path, skipping all commented and empty lines before the csv table header.
    :param path:
    :param prefix:
    """
    with open(path, encoding='utf-8') as file:
        body = dropwhile(lambda x: str.startswith(x, prefix), file)
        lines = (s.rstrip() for s in body if s.rstrip())

        yield from lines


def include_events(rows, event_names, columns=None):
    """
Filter rows to only the desired event names and outputs selected columns.
    :param rows:
    :param event_names:
    :param columns:
    """
    include = set(event_names)
    for row in rows:
        row_events = row['EventSource'].split('|')
        if len(include.intersection(row_events)) > 0:
            if columns:
                row = {col: row[col] for col in columns if col in row}
            yield row


def filter_rows(rows, events, columns=None):
    """
Parses rows from a csv and yields rows with the desired events.
    :param rows: Iterator of strings from a csv file, including headers.
    :param events: Names of events to include. Only rows with at least one of the events
                    in the list will be returned.
    :param columns: Optional list of keys to include in output. If None, all keys will be returned.
    :return: 
    """
    reader = csv.DictReader(rows, delimiter='\t')
    test_slides = (line for line in reader if line['SlideType'] == 'TestImage')
    yield from include_events(test_slides, events, columns)


def process_file_to_csv(path, outdir='out/', columns=None):
    """
Process the given file and saves it to outdir as a csv
    :param path:
    :param outdir:
    :param columns:
    """
    data = skip_comments(path)
    filtered = filter_rows(data, ['ABMBrainState'], columns)
    try:
        first = next(filtered)

        base = os.path.basename(path)
        path = outdir + os.path.splitext(base)[0] + '.csv'
        print('Parsing', base)
        with open(path, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=first.keys(), extrasaction='ignore')
            writer.writeheader()
            writer.writerow(first)

            writer.writerows(filtered)
    except StopIteration as e:
        print("FAILED TO PARSE ", path, e)


def process_file_to_db(path, db_path, events, table, columns=None):
    """
Process given file and saves the output to the specified database file.
    :param path:
    :param db_path:
    :param events:
    :param table:
    :param columns:
    """
    db = dataset.connect('sqlite:///' + db_path)
    table = db[table]
    rows = skip_comments(path)
    filtered = filter_rows(rows, events, columns)
    table.insert_many(filtered)


if __name__ == '__main__':
    # file_path = 'sample_data/ABM.txt'
    files = glob.glob("D:\\Adidas 1.1\\adidas 1.11\\WMC\*.txt")
    outdir = 'out/'
    selected_columns = [
        # Study and participant data
        'StudyName',
        # 'ExportDate',
        'Name',
        'Age',
        'Gender',
        # 'StimuliBlock',
        'StimulusName',
        # 'SlideType',
        # 'EventSource',
        'Timestamp',
        # 'MediaTime',
        # 'TimeSignal',

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
    ]
    # process_file_to_csv(file_path, columns=selected_columns)
    # process_file_to_db(file_path, 'sample.db', ['ABMBrainState'], 'eeg', columns=selected_columns)
    for file in files:
        print('Processing:', file)
        process_file_to_db(file, 'WMC.db', ['ABMBrainState'], 'eeg', selected_columns)
