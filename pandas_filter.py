import sys

import os.path
import glob
from utils import read_events, read_cols, process_file


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
    except ValueError as e:
        print("Could not process ", path, file=sys.stderr)
        print(e, file=sys.stderr)
        print("Events found: ", read_events(path), file=sys.stderr)
        print("Columns found: ", read_cols(path), file=sys.stderr)


if __name__ == '__main__':
    from multiprocessing import Pool
    from functools import partial

    destination_dir = "out/adidas runners S2/affdex/"
    events = ['ABMBrainState', ]

    add_columns = None  # {'FixationAOI': str}

    files = glob.glob('data/adidas runners S2/*')
    for file in files:
        process_to_csv(file, out_dir=destination_dir, event_sources=events, add_types=add_columns)
    # func = partial(process_to_csv, out_dir=destination_dir, event_sources=events,
    #                add_types=add_columns)
    #
    # pool = Pool(1)  # Leave at 1 if IO bound to reduce read contention on disk
    # pool.map(func, files)
    # pool.close()
    # pool.join()
