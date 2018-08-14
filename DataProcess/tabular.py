import csv
from itertools import dropwhile


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


if __name__ == '__main__':
    file_path = 'sample_data/059_230.txt'
    data = skip_comments(file_path)
    filtered = filter_rows(data, ['ABMBrainState'])

    for f in filtered:
        cols = ['Name', 'Age', 'Gender', 'StimulusName', 'EventSource', 'Classification']
        subset = {col: f[col] for col in cols if col in f}
        print(subset)
