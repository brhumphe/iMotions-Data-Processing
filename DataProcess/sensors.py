import pandas as pd
from abc import ABC, abstractmethod
from typing import Dict, List, Callable, ClassVar
import numpy as np

FilterRule = Callable[[pd.DataFrame], pd.Series]


class EventSource(ABC):
    """
    A data source in an iMotions data file
    """
    source_name: ClassVar[str]
    out_columns: ClassVar[List[str]]
    dtypes: ClassVar[Dict[str, type]]
    include: ClassVar[List[FilterRule]] = []
    exclude: ClassVar[List[FilterRule]] = []


class Affdex(EventSource):

    @staticmethod
    def filter_num_faces(df):
        return df['Number of faces'] == 1

    include = [filter_num_faces]

    dtypes = {
        'Number of faces': np.float64,
        # 'width': np.float64,
        # 'height': np.float64,
        # 'FrameIndex': np.float64,
        # 'faceid': np.float64,
        # '#classifiers': np.float64,
        # 'Brow Furrow': np.float64,
        # 'Brow Raise': np.float64,
        'Engagement': np.float64,
        # 'Lip Corner Depressor': np.float64,
        'Smile': np.float64,
        'Valence': np.float64,
        'Attention': np.float64,
        # 'Interocular Distance': np.float64,
        # 'Pitch': np.float64,
        # 'Yaw': np.float64,
        # 'Roll': np.float64,
        # 'InnerBrowRaise': np.float64,
        # 'EyeClosure': np.float64,
        # 'NoseWrinkle': np.float64,
        # 'UpperLipRaise': np.float64,
        # 'LipSuck': np.float64,
        # 'LipPress': np.float64,
        # 'MouthOpen': np.float64,
        # 'ChinRaise': np.float64,
        # 'Smirk': np.float64,
        # 'LipPucker': np.float64,
        'Anger': np.float64,
        'Sadness': np.float64,
        'Disgust': np.float64,
        'Joy': np.float64,
        'Surprise': np.float64,
        'Fear': np.float64,
    }


class ABMBrainState(EventSource):
    """
    Advanced Brain Monitoring Constructs
    """
    dtypes = {
            'Classification': np.float64,
            'HighEngagement': np.float64,
            'LowEngagement': np.float64,
            'Distraction': np.float64,
            'Drowsy': np.float64,
            'WorkloadFBDS': np.float64,
            'WorkloadBDS': np.float64,
            'WorkloadAverage': np.float64
        }

    @staticmethod
    def filter_classification(df):
        return df['Classification'] > 0

    include = [filter_classification]
