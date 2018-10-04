import pandas as pd
import attr
from utils import read_cols, read_events


@attr.s
class Session:
    """
    Represents a single file of iMotions data. Assumes only one participant per file.
    """
    path = attr.ib()
    _cols = attr.ib(init=False, default=None)
    _dtypes = attr.ib(init=False, default=None)
    _events = attr.ib(init=False, default=None)

    @property
    def cols(self):
        if not self._cols:
            self._cols = read_cols(self.path)
        return self._cols

    @property
    def events(self):
        if not self._events:
            self._events = read_events(self.path)
        return self._events

    def __contains__(self, item):
        """Want to check EventSource Membership. E.g.
        > if ABMBrainState in Session: ...
        """
