import sys

import os.path
import glob
from utils import read_events, read_cols, process_file
import numpy as np


def process_to_csv(path, out_dir, event_sources, add_types=None):
    """
Process file and saves results to CSV in output directory.
    :param path:
    :param out_dir:
    :param event_sources:
    :param add_types:
    """
    print("Cleaning ", path)
    base_name = os.path.basename(path)
    try:
        df = process_file(path, event_sources, add_types=add_types)

        out_path = out_dir + os.path.splitext(base_name)[0] + '.csv'
        # TODO: Move this test up into main filter function
        df[df['SlideType'] == 'TestImage'].to_csv(out_path, index=False)
    except Exception as e:
        print("Could not process ", path, file=sys.stderr)
        print(e, file=sys.stderr)
        print("Events found: ", read_events(path), file=sys.stderr)
        print("Columns found: ", read_cols(path), file=sys.stderr)


if __name__ == '__main__':
    # See `sensors.py` for sensor definitions
    events = ['ET', ]

    # Columns and their types not specified in `sensors.py`
    add_columns = {'UTCTimestamp': str,
                   'MediaTime': np.float,
                   'TimeSignal': np.float,
                   }  # {'FixationAOI': str}
    # add_columns = None
    files = glob.glob('data/nyc flagship store/*')
    destination_dir = "out/nyc flagship store ET cleaned/"
    for file in files:
        process_to_csv(file, out_dir=destination_dir, event_sources=events, add_types=add_columns)

    # Uncomment the following to speed up processing if you have the data on an SSD.
    # from multiprocessing import Pool
    # from functools import partial
    # func = partial(process_to_csv, out_dir=destination_dir, event_sources=events,
    #                add_types=add_columns)

    # pool = Pool(4)  # Leave at 1 if IO bound (I.E. not using an SSD) to reduce read contention on disk
    # pool.map(func, files)
    # pool.close()
    # pool.join()
