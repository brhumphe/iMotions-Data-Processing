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


# TODO: Rewrite to be inclusive instead of exclusive
def remove_events(rows, remove):
    """
Returns rows which contain events besides those in remove.
    :param rows: An iterable of dicts from a data file with the 'EventSource' key
    :param remove: List of events which should be ignored.
    """
    for row in rows:
        row_source__split = row['EventSource'].split('|')
        for r in remove:
            if r in row_source__split:
                row_source__split.remove(r)

        # Yield only lines that have remaining events
        if row_source__split:
            yield row


def filter_rows(rows, remove):
    """
Returns rows with valid data
    :param rows: 
    :param remove: 
    :return: 
    """
    reader = csv.DictReader(rows, delimiter='\t')
    test_slides = (line for line in reader if line['SlideType'] == 'TestImage')
    events = remove_events(test_slides, remove)
    return events


if __name__ == '__main__':
    file_path = 'sample_data/059_230.txt'
    data = skip_comments(file_path)
    filtered = filter_rows(data, ['ABMRawEEG', 'ABMDeconEEG'])

    for f in filtered:
        print(f)
