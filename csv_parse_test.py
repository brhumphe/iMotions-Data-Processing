from itertools import filterfalse, islice, dropwhile
import csv
from pprint import pprint


def remove_events(events, remove):
    for event in events:
        event_source__split = event['EventSource'].split('|')
        for r in remove:
            if r in event_source__split:
                event_source__split.remove(r)

        if event_source__split:
            yield event


def filter_rows(lines, remove):
    reader = csv.DictReader(lines, delimiter='\t')
    test_slides = (line for line in reader if line['SlideType'] == 'TestImage')
    events = remove_events(test_slides, remove)
    return events


def parse_export(path, remove=None):
    if remove is None:
        remove = ['ABMRawEEG', 'ABMDeconEEG']

    with open(path, encoding='utf-8') as file:
        body = dropwhile(lambda x: str.startswith(x, '#'), file)
        lines = (s.rstrip() for s in body if s.rstrip())

        yield from (filter_rows(lines, remove))


file_path = 'sample_data/059_230.txt'

for e in parse_export(file_path):
    print(e)
