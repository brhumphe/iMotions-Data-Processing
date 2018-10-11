import logging

import pandas as pd
from sensors import EventNames, STUDY_INFO


def read_events(file):
    """
Examines the first nrows of a file and returns unique event sources
    :param file:
    :return: Set of EventSource names
    """
    df = pd.read_csv(file, sep='\t', usecols=['EventSource'], nrows=5000, comment='#')
    return {e for event in list(df['EventSource'])
            for e in event.split('|')}


def read_cols(file):
    """
Returns a list of all columns present in a file.
    :param file:
    :return:
    """
    df = pd.read_csv(file, sep='\t', nrows=1, comment='#')
    return list(df.columns)


def generate_types(file, event_sources):
    """
Given a file and list of strings of event names as they appear in the EventSource column, creates a dict
of types for use by pandas.read_csv
    :param file:
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


def open_file(filename, event_sources, chunksize=10000):
    types = None
    cols = None

    if event_sources:
        types = generate_types(filename, event_sources)
        cols = list(types.keys())
    return pd.read_csv(filename, sep='\t', encoding='utf-8', chunksize=chunksize, dtype=types,
                       comment='#', skip_blank_lines=True, usecols=cols)


def filter_events(df, events):
    """
Filters df to include only rows where EventSource includes at least one of the valid events.
    :param df:
    :param events: List of string names of event sources
    :return:
    """
    f = []
    for e in events:
        f.append(df['EventSource'].str.contains(e))

    event_rows = pd.concat(f, axis=1).any(axis=1)
    return df[event_rows]
