from abc import ABC, abstractmethod
from typing import Dict, List
from .fast_filter import FilterRule

import numpy as np


class EventSource(ABC):
    """
    A data source in an iMotions data file
    """
    @property
    @abstractmethod
    def dtypes(self) -> Dict[str, type]:
        pass

    @property
    def include(self) -> List[FilterRule]:
        return []

    @property
    def exclude(self) -> List[FilterRule]:
        return []


class ABMBrainState(EventSource):
    """
    Advanced Brain Monitoring Constructs
    """
    @property
    def dtypes(self) -> Dict[str, type]:
        return {
            'Classification': np.float64,
            'HighEngagement': np.float64,
            'LowEngagement': np.float64,
            'Distraction': np.float64,
            'Drowsy': np.float64,
            'WorkloadFBDS': np.float64,
            'WorkloadBDS': np.float64,
            'WorkloadAverage': np.float64
        }

    @property
    def include(self) -> List[FilterRule]:
        return [self.filter_classification]

    @staticmethod
    def filter_classification(df):
        return df['Classification'] > 0
