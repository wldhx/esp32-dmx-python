import asyncio
from pyartnet import ArtNetNode


class Flood:
    def __init__(self, universe, start: int):
        self.master = universe.add_channel(start, width=1)
        self.r = universe.add_channel(start + 1, width=1)
        self.g = universe.add_channel(start + 2, width=1)
        self.b = universe.add_channel(start + 3, width=1)


class Eve:
    def __init__(self, universe, start: int):
        self.x = universe.add_channel(start, width=1)
        self.y = universe.add_channel(start + 2, width=1)
        self.master = universe.add_channel(start + 7, width=1)
        self.strobe = universe.add_channel(start + 8, width=1)
        self.r = universe.add_channel(start + 9, width=1)
        self.g = universe.add_channel(start + 10, width=1)
        self.b = universe.add_channel(start + 11, width=1)
        self.w = universe.add_channel(start + 12, width=1)
        self.laser = universe.add_channel(start + 13, width=1)
        self.laser_strobe = universe.add_channel(start + 14, width=1)


async def fade(ch, *args):
    """Add fade and wait until it completes."""
    ch.add_fade(*args)
    await ch.wait_till_fade_complete()


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

    async def yellow_pulse(obj):
        await fade(obj.g, [40], 10000)
        await fade(obj.g, [0], 10000)

    while True:
        await asyncio.gather(circle(), yellow_pulse(eve), yellow_pulse(flood))


asyncio.run(main())
