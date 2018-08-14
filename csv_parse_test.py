from itertools import filterfalse, islice, dropwhile
import csv
from pprint import pprint

file_path = 'data/Scarcity/001_p101.txt'

with open(file_path, encoding='utf-8') as file:
    body = dropwhile(lambda x: str.startswith(x, '#'), file)
    lines = (s.rstrip() for s in body if s.rstrip())

    reader = csv.DictReader(lines, delimiter='\t')
    test_slides = (line for line in reader if line['SlideType'] == 'TestImage')

    for s in islice(test_slides, 5):
        print(s)

