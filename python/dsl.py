import asyncio
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import *
from utils import *


@dataclass(frozen=True)
class Op:
    def __await__(self):
        pass


@dataclass(frozen=True)
class Sleep(Op):
    duration_ms: int

    def __await__(self):
        yield from sleep(self.duration_ms).__await__()


@dataclass(frozen=True)
class Fade(Op):
    ch: Any
    target_values: Tuple[int]
    duration_ms: int

    def __await__(self):
        yield from fade(self.ch, self.target_values, self.duration_ms).__await__()


@dataclass(frozen=True)
class WaitAll(Op):
    ops: Tuple[Op]  # XXX: consider taking ops as *args

    def __await__(self):
        # XXX
        coros = []
        for op in self.ops:

            async def coro():
                await op

            coros.append(coro())

        yield from asyncio.gather(*coros).__await__()


@dataclass(frozen=True)
class Seq(Op):
    ops: Tuple[Op]

    def __await__(self):
        for op in self.ops:
            yield from op.__await__()


@dataclass(frozen=True)
class Debug(Op):
    message: str
    op: Op

    def __await__(self):
        print(self.message)
        yield from self.op.__await__()
