import csv
import glob
import os
from itertools import dropwhile
from multiprocessing import Pool


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


def include_events(rows, event_names):
    include = set(event_names)
    for row in rows:
        row_events = row['EventSource'].split('|')
        if len(include.intersection(row_events)) > 0:
            yield row


def filter_rows(rows, events):
    """
Parses rows from a csv and yields rows with the desired events.
    :param rows: Iterator of strings from a csv file, including headers.
    :param events: Names of events to include. Only rows with at least one of the events
                    in the list will be returned.
    :return: 
    """
    reader = csv.DictReader(rows, delimiter='\t')
    test_slides = (line for line in reader if line['SlideType'] == 'TestImage')
    yield from include_events(test_slides, events)


def process_file(path, outdir='out/'):
    data = skip_comments(path)
    filtered = filter_rows(data, ['ABMBrainState'])
    try:
        first = next(filtered)

        base = os.path.basename(path)
        path = outdir + os.path.splitext(base)[0] + '.csv'
        print('Parsing', base)
        with open(path, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=first.keys())
            writer.writeheader()
            writer.writerow(first)

            writer.writerows(filtered)
    except StopIteration as e:
        print("FAILED TO PARSE ", path, e)


if __name__ == '__main__':
    file_path = 'sample_data/059_230.txt'
    files = glob.glob("D:\\Adidas 1.1\\adidas 1.11\\ToL/*.txt")
    outdir = 'out/'

    pool = Pool()
    pool.map(process_file, files)
    # for file_path in files:
    #     process_file(file_path)

        # for f in filtered:
        #     cols = ['Name', 'Age', 'Gender', 'StimulusName', 'EventSource', 'Classification']
        #     subset = {col: f[col] for col in cols if col in f}
        #     print(subset)
