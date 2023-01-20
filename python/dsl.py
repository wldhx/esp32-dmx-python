from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import *
from utils import *


@dataclass
class Op(ABC):
    @abstractmethod
    def __await__(self):
        pass


@dataclass
class Sleep(Op):
    duration_ms: int

    def __await__(self):
        yield from sleep(self.duration_ms).__await__()


@dataclass
class Fade(Op):
    ch: Any
    target_values: Any
    duration_ms: int

    def __await__(self):
        yield from fade(self.ch, self.target_values, self.duration_ms).__await__()
