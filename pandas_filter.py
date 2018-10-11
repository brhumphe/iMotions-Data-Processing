import sys

import pandas as pd
import os.path
import glob
from utils import open_file, filter_events, read_events, read_cols


def process_file(filename, event_sources, add_types=None, chunksize=50000):
    data = open_file(filename, event_sources, add_types=add_types, chunksize=chunksize)
    frames = []
    for chunk in data:
        frames.append(filter_events(chunk, event_sources))
    return pd.concat(frames)


def process_to_csv(path, out_dir, event_sources):
    print("Cleaning ", path)
    base_name = os.path.basename(path)
    try:
        df = process_file(path, event_sources)

        out_path = out_dir + os.path.splitext(base_name)[0] + '.csv'
        df[df['SlideType'] == 'TestImage'].to_csv(out_path, index=False)
    except ValueError as e:
        print("Count not process ", path, file=sys.stderr)
        print(e, file=sys.stderr)
        print(read_events(path))
        print(read_cols(path))


if __name__ == '__main__':
    from multiprocessing import Pool
    from functools import partial

    destination_dir = "out/r111/"
    events = ['Performance Metrics Epoc']

    files = glob.glob("data/001_r111/*.txt")
    func = partial(process_to_csv, out_dir=destination_dir, event_sources=events)

    pool = Pool(1)  # Leave at 1 if IO bound to reduce read contention on disk
    pool.map(func, files)
    pool.close()
    pool.join()
