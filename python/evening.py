import asyncio
from pyartnet import ArtNetNode
from fixtures import *
from utils import *
from dsl import *

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

    @forever
    async def eve_move():
        seq = (
            WaitAll(
                (
                    Seq(
                        (
                            Fade(eve.x, (10,), MULTIPLIER),  # to kitchen door
                            Fade(eve.x, (20,), MULTIPLIER * 2),  # kitchen door
                            Sleep(MULTIPLIER),
                        )
                    ),
                    Fade(eve.y, (15,), MULTIPLIER * 4),  # kitchen door
                )
            ),
            WaitAll(
                (
                    Fade(eve.x, (65,), MULTIPLIER * 2),  # to entrance door
                    Seq(
                        (
                            Fade(eve.y, (120,), MULTIPLIER),  # transition
                            Fade(eve.y, (30,), MULTIPLIER),  # to entrance door
                        )
                    ),
                )
            ),
            WaitAll(
                (
                    Fade(eve.x, (70,), MULTIPLIER * 2),  # entrance door
                    Seq(
                        (
                            Fade(eve.y, (55,), MULTIPLIER),  # entrance door
                            Sleep(MULTIPLIER),
                        )
                    ),
                )
            ),
            WaitAll(
                (
                    Fade(eve.x, (170,), MULTIPLIER * 4),  # 360 turn
                    Fade(eve.y, (140,), MULTIPLIER * 4),  # 360 turn
                )
            ),
        )
        await Seq(seq + seq[::-1])

    @forever
    async def yellow_pulse(obj):
        await fade(obj.g, [20], MULTIPLIER)
        await sleep(MULTIPLIER * 2)
        await fade(obj.g, [0], MULTIPLIER)
        await sleep(MULTIPLIER * 2)

    await asyncio.gather(eve_move(), yellow_pulse(eve), yellow_pulse(flood))


asyncio.run(main())
