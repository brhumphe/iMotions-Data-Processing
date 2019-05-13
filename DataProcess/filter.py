# Given a data frame we need to return only the desired subset
# according to a user-specified list of rules. To maintain performance,
# each filter will return a boolean index, and the boolean indices assembled
# into the final boolean index which will determine the output data frame.
import itertools
import collections
from typing import Callable, List, Type
import pandas as pd

# A FilterRule should return a boolean index denoting which rows of the dataframe
# should be included.
from DataProcess.fast_filter import fast_filter
from DataProcess.sensors import EventSource


class Filter:
    """
Filters the provided data for rows with valid event sources.
    """
    def __init__(self, event_sources: List[Type[EventSource]]):
        self.source_names = [e.source_name for e in event_sources]
        self.columns = [e.out_columns for e in event_sources]

        includes = [e.include for e in event_sources]
        self.include_rules = list(itertools.chain(*includes))

        excludes = [e.exclude for e in event_sources]
        self.exclude_rules = list(itertools.chain(*excludes))

        dtypes = [e.dtypes for e in event_sources]
        self.dtypes = dict(collections.ChainMap(*dtypes))

    def filter(self, df: pd.DataFrame) -> pd.DataFrame:
        include_indices = []
        for rule in self.include_rules:
            # WARNING!!! Assumes that filtering rules are static methods on the EventSource object!!!
            include_indices.append(rule.__func__(df))

        include_rows = pd.concat(include_indices, axis=1).any(axis=1)
        # return df[include_rows]

        exclude_indices = []
        for rule in self.exclude_rules:
            exclude_indices.append(rule.__func__(df))

        exclude_rows = pd.concat(exclude_indices, axis=1).any(axis=1)

        return df[include_rows & ~ exclude_rows]
