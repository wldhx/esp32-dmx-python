import asyncio
from pyartnet import ArtNetNode
import random
from itertools import *
from fixtures import *
from dsl import *
from utils import *


SLEEP = 100


async def main():
    node = ArtNetNode("10.255.255.255", broadcast=True)
    await node.start()

    universe = node.add_universe(0)

    laser = F0Laser(universe, 1)
    f0floods = [
        F0Flood(universe, i)
        for i in (
            10,
            20,
        )
    ]
    flood = Flood(universe, 30)
    eve = Eve(universe, 40)

    await WaitAll(
        (
            Fade(flood.master, (100,), 0),
            *[Fade(f.master, (255,), 0) for f in f0floods],
            Fade(eve.master, (100,), 0),
            Fade(eve.r, (255,), 0),
            Fade(eve.laser, (10,), 0),
        )
    )

    async def pulse_red(fixture):
        await Seq(
            (
                Fade(fixture.r, (255,), SLEEP),
                Fade(fixture.r, (80,), SLEEP),
            )
        )

    async def rainbow(fixture):
        await Seq(
            (
                Fade(fixture.r, (255,), SLEEP * 5),
                Fade(fixture.r, (0,), SLEEP * 5),
                Fade(fixture.g, (255,), SLEEP * 5),
                Fade(fixture.g, (0,), SLEEP * 5),
                Fade(fixture.b, (255,), SLEEP * 5),
                Fade(fixture.b, (0,), SLEEP * 5),
            )
        )

    async def random_master(fixture):
        await Seq(
            (
                Fade(fixture.master, (random.randint(0, 255),), SLEEP),
                Sleep(random.randint(0, SLEEP)),
            )
        )

    async def random_fade(fixture):
        await Seq(
            (
                Fade(fixture.r, (random.randint(0, 255),), SLEEP),
                Fade(fixture.g, (random.randint(0, 255),), SLEEP),
                Fade(fixture.b, (random.randint(0, 255),), SLEEP),
            )
        )

    async def eve_scan():
        await Seq(
            (
                Fade(eve.x, (10,), SLEEP * 5),
                Fade(eve.x, (20,), SLEEP * 5),
                Fade(eve.x, (65,), SLEEP * 5),
                Fade(eve.x, (70,), SLEEP * 5),
                Fade(eve.x, (10,), SLEEP * 5),
            )
        )

    await WaitAll(
        (
            Seq(
                (
                    *(pulse_red(flood) for _ in range(3)),
                    rainbow(flood),
                )
            ),
            # Seq(
            #     (
            #         Fade(laser.animation_mode, (100,), 0),
            #         Sleep(1000),
            #     )
            # ),
            # WaitAll(
            #     (
            #         Seq((*[random_fade(f) for f in f0floods],)),
            #         Seq((*[random_master(f) for f in f0floods],)),
            #     )
            # ),
            eve_scan(),
        )
    )


asyncio.run(main())
