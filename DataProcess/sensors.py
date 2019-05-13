import pandas as pd
from abc import ABC, abstractmethod, abstractproperty, abstractclassmethod
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
    source_name = "AffRaw"

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


class ET(EventSource):
    """
    Tobii Eye Tracker
    """

    @property
    def exclude(self) -> List[FilterRule]:
        return []

    source_name = 'ET'
    dtypes = {
        'ValidityLeft': np.float,
        'ValidityRight': np.float,
        'PupilLeft': np.float,
        'PupilRight': np.float,
        'FixationX': np.float,
        'FixationY': np.float,
        'FixationAOI': str,
        'FixationStart': np.float,  # Double check this
        'FixationDuration': np.float,
        'FixationSeq': np.float,
        'AccX': np.float,
        'AccY': np.float,
        'AccZ': np.float,
        'GyroX': np.float,
        'GyroY': np.float,
        'GyroZ': np.float,
        'Gaze3DX': np.float,
        'Gaze3DY': np.float,
        'Gaze3DZ': np.float,
        'Distance3D': np.float,
        'GazeDirectionLeftX': np.float,
        'GazeDirectionLeftY': np.float,
        'GazeDirectionLeftZ': np.float,
        'GazeDirectionRightX': np.float,
        'GazeDirectionRightY': np.float,
        'GazeDirectionRightZ': np.float,
        'GazeX': np.float,
        'GazeY': np.float,
        'GazeAOI': np.float,
        'InterpolatedGazeX': np.float,
        'InterpolatedGazeY': np.float,
        'GazeEventType': np.float,
        'GazeVelocityAngle': np.float,
        'SaccadeSeq': np.float,
        'SaccadeStart': np.float,
        'SaccadeDuration': np.float,
    }

    @staticmethod
    def filter_valid(df):
        return df['ValidityLeft'] == 0 and df['ValidityRight'] == 0

    include = [filter_valid]
