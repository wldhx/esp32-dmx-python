import asyncio
from pyartnet import ArtNetNode
from common import *

MULTIPLIER = 5000


async def main():
    node = ArtNetNode("192.168.31.255", broadcast=True)
    await node.start()

    universe = node.add_universe(0)

    eve = Eve(universe, 1)
    flood = Flood(universe, 18)

    await fade(eve.master, [30], 0)
    await fade(eve.r, [255], 0)
    await fade(eve.y, [90], 0)

    await fade(flood.master, [255], 0)
    await fade(flood.r, [255], 0)

    async def circle():
        await fade(eve.x, [255], MULTIPLIER * 4)
        await fade(eve.x, [0], MULTIPLIER * 4)

    async def eve_x():
        seq = [
            (eve.x, [10], MULTIPLIER),  # to kitchen door
            (eve.x, [15], MULTIPLIER * 2),  # kitchen door
            (eve.x, [20], MULTIPLIER),  # kitchen door
            (eve.x, [65], MULTIPLIER * 2),  # to entrance door
            (eve.x, [70], MULTIPLIER * 2),  # entrance door
            (eve.x, [170], MULTIPLIER * 4),  # 360 turn
        ]

        [await fade(*x) for x in seq]
        # [await fade(*x) for x in seq[::-1]]

    async def eve_y():
        seq = [
            (eve.y, [15], MULTIPLIER * 4),  # kitchen door
            (eve.y, [120], MULTIPLIER),  # transition
            (eve.y, [30], MULTIPLIER),  # to entrance door
            (eve.y, [55], MULTIPLIER * 2),  # entrance door
            (eve.y, [140], MULTIPLIER * 4),  # 360 turn
        ]

        [await fade(*x) for x in seq]
        # [await fade(*x) for x in seq[::-1]]

    async def yellow_pulse(obj):
        await fade(obj.g, [40], MULTIPLIER * 6)
        await fade(obj.g, [0], MULTIPLIER * 6)

    while True:
        await asyncio.gather(eve_x(), eve_y(), yellow_pulse(eve), yellow_pulse(flood))


asyncio.run(main())
