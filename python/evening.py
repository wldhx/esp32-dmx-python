import asyncio
from pyartnet import ArtNetNode
from common import *


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
        await fade(eve.x, [255], 20000)
        await fade(eve.x, [0], 20000)

    async def eve_cover_doors():
        await wait(
            [eve.x, eve.y],
            lambda: (
                eve.x.add_fade([20], 10000),  # kitchen door
                eve.y.add_fade([30], 4000),
            ),
        )

        await wait(
            [eve.x, eve.y],
            lambda: (
                eve.x.add_fade([70], 10000),  # entrance door
                eve.y.add_fade([45], 4000),
            ),
        )

        await wait(
            [eve.x, eve.y],
            lambda: (
                eve.x.add_fade([170], 10000),  # 360 turn
                eve.y.add_fade([90], 4000),
            ),
        )

    async def yellow_pulse(obj):
        await fade(obj.g, [40], 10000)
        await fade(obj.g, [0], 10000)

    while True:
        await asyncio.gather(eve_cover_doors(), yellow_pulse(eve), yellow_pulse(flood))


asyncio.run(main())
