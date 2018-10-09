import logging

import pandas as pd


def read_events(filename):
    """
Examines the first nrows of a file and returns unique event sources
    :param filename:
    :return: Set of EventSource names
    """
    df = pd.read_csv(filename, sep='\t', usecols=['EventSource'], nrows=5000, comment='#')
    return {e for event in list(df['EventSource'])
            for e in event.split('|')}


def read_cols(filename):
    """
Returns a list of all columns present in a file.
    :param filename:
    :return:
    """
    df = pd.read_csv(filename, sep='\t', nrows=1, comment='#')
    return list(df.columns)


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
