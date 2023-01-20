import asyncio
from pyartnet import ArtNetNode
import random
from utils import *
from dsl import *
from fixtures import Flood


async def main():
    node = ArtNetNode("192.168.31.255", broadcast=True)
    await node.start()

    universe = node.add_universe(0)
    flood = Flood(universe, 18)

    await Fade(flood.master, [100], 0)
    await Fade(flood.r, [255], 0)

    seq = [
        Debug("r->g", WaitAll([Fade(flood.r, [0], 1000), Fade(flood.g, [255], 1000)])),
        Sleep(1000),
        Debug("g->r", WaitAll([Fade(flood.r, [255], 1000), Fade(flood.g, [0], 1000)])),
    ]
    [await x for x in seq]
    [await x for x in seq[::-1]]


asyncio.run(main())
