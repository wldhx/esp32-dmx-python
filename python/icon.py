import asyncio
from pyartnet import ArtNetNode
import random
from fixtures import Eve
from utils import *


async def main():
    node = ArtNetNode("192.168.31.255", broadcast=True)
    await node.start()

    universe = node.add_universe(0)

    eve = Eve(universe, 1)

    await fade(eve.laser, [20], 0)

    await fade(eve.master, [10], 0)
    await fade(eve.r, [130], 0)
    await fade(eve.g, [16], 0)
    await fade(eve.b, [130], 0)

    while True:
        sign = 1 if random.random() > 0.5 else -1
        dx = random.randint(0, 10)

        x = 120 + sign * dx
        y = random.randint(0, 20)
        in_icon = x > 116 and x < 122 and y > 2 and y < 15

        speed = random.randint(200, 1000)

        async def brightness():
            very_bright = random.random() > 0.9

            if in_icon:
                await fade(eve.laser, [255 if very_bright else 100], speed)
            else:
                await fade(eve.laser, [10], speed)

        async def move():
            await wait(
                [eve.x, eve.y],
                lambda: (
                    eve.x.add_fade([x], speed),
                    eve.y.add_fade([y], speed),
                ),
            )

        await asyncio.gather(brightness(), move())


asyncio.run(main())
