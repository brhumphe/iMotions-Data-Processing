import sys

import pandas as pd
import os.path
import glob
from utils import open_file, filter_events, read_events, read_cols
from zipfile import ZipFile


def process_file(filename, event_sources, add_types=None, chunksize=50000):
    data = open_file(filename, event_sources, add_types=add_types, chunksize=chunksize)
    frames = []
    for chunk in data:
        frames.append(filter_events(chunk, event_sources))
    return pd.concat(frames)


out_dir = "out/ecomm/"

archive = ZipFile("data/Sensor Data.zip")
# files = [info.filename for info in archive.infolist()]
events = ['ABMBrainState']

for file in glob.glob("data/Sensor Data/*.txt"):
        print("Cleaning ", file)
        base_name = os.path.basename(file)
        try:
            df = process_file(file, events)

            out_path = out_dir + os.path.splitext(base_name)[0] + '.csv'
            df[df['SlideType'] == 'TestImage'].to_csv(out_path, index=False)
        except ValueError as e:
            print("Count not process ", file, file=sys.stderr)
            print(e, file=sys.stderr)
            print(read_events(file))
            print(read_cols(file))
