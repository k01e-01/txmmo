from types import SimpleNamespace
from typing import Any


class State(SimpleNamespace):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.data = {}
        self.actions = {}
