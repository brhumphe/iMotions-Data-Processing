import pandas as pd


def read_events(filename):
    df = pd.read_csv(filename, sep='\t', usecols=['EventSource'], nrows=5000, comment='#')
    return {e for event in list(df['EventSource'])
            for e in event.split('|')}


def read_cols(filename):
    df = pd.read_csv(filename, sep='\t', nrows=1, comment='#')
    return list(df.columns)
