import logging
import pandas as pd

from sensors import EventNames, STUDY_INFO


def read_events(file, nrows=5000):
    """
Examines the first nrows of a file and returns unique event sources
    :param file: File name or file-like object compatible with `pandas.read_csv`
    :param nrows: Number of rows to scan for EventSources
    :return: Set of EventSource names
    """
    df = pd.read_csv(file, sep='\t', usecols=['EventSource'], nrows=nrows, comment='#')
    return {e for event in list(df['EventSource'])
            for e in event.split('|')}


def read_cols(file):
    """
Returns a list of all columns present in a file.
    :param file: File name or file-like object compatible with `pandas.read_csv`
    :return: List of column names
    """
    df = pd.read_csv(file, sep='\t', nrows=1, comment='#')
    return list(df.columns)


def generate_types(file, event_sources):
    """
Given a file and list of strings of event names as they appear in the EventSource column, creates a dict
of types for use by pandas.read_csv
    :param file: File name or file-like object compatible with `pandas.read_csv`
    :param event_sources:
    :return:
    """
    file_events = read_events(file)

    invalid_events = set(event_sources) - set(EventNames.keys())
    if invalid_events:
        raise ValueError(f"Unsupported events:{invalid_events}")

    missing_events = set(event_sources) - set(file_events)
    if missing_events:
        raise ValueError(f"Expected event sources not found: {missing_events}")

    types = STUDY_INFO
    for e in event_sources:
        types.update(EventNames[e])

    logging.debug("Using types: %s", types)

    return types


def run_sql_file(sql_file, connection):
    """
Executes the contents of sql_file on the database connection.
    :param sql_file:
    :param connection:
    """
    print("Executing ", sql_file)
    logging.debug("Executing %s", sql_file)
    try:
        with open(sql_file, 'r', encoding='utf-8') as fd:
            sql_file = fd.read()
            connection.executescript(sql_file)
    except Exception as e:
        logging.exception("Failed to run %s\n%s", sql_file, e)


def open_file(filename, event_sources, *, add_types=None, chunksize=10000):
    """
Parses a text file of data, returning only the specified columns and event sources
    :param filename: File name or file-like object compatible with `pandas.read_csv`
    :param event_sources: List of event names as shown in EventSource column
    :param add_types: Additional column:dtype dict for extra columns beyond those of the supplied event sources.
    :param chunksize: Number of rows to process per-iteration
    :return: Pandas csv reader object
    """
    if add_types is None:
        add_types = {}
    types = None
    cols = None

    if event_sources:
        types = {**generate_types(filename, event_sources), **add_types}
        cols = list(types.keys())

    return pd.read_csv(filename, sep='\t', encoding='utf-8', chunksize=chunksize, dtype=types,
                       comment='#', skip_blank_lines=True, usecols=cols)


def filter_event_source(df, events):
    """
Filters df to include only rows where EventSource includes at least one of the valid events.
    :param df: DataFrame to filter
    :param events: List of string names of event sources
    :return: Filtered DataFrame
    """
    f = []
    for e in events:
        # Creates a boolean series of rows that contains event e
        contains = df['EventSource'].str.contains(e)
        f.append(contains)

    # Logical OR of all boolean series in f
    event_rows = pd.concat(f, axis=1).any(axis=1)

    # Returns only rows where event_rows == True
    return df[event_rows]


def process_file(filename, event_sources, add_types=None, chunksize=50000):
    """
Processes a file and returns a DataFrame of the cleaned data
    :param filename:
    :param event_sources: List of strings of EventSource names
    :param add_types: Additional columns to include and their dtype
    :param chunksize: Rows to process per batch
    :return: Resulting DataFrame
    """
    data = open_file(filename, event_sources, add_types=add_types, chunksize=chunksize)
    frames = []
    for chunk in data:
        frames.append(filter_event_source(chunk, event_sources))
    return pd.concat(frames)
