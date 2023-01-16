import asyncio
from pyartnet import ArtNetNode


async def fade(ch, *args):
    """Add fade and wait until it completes."""
    ch.add_fade(*args)
    await ch.wait_till_fade_complete()


async def wait(chs, f):
    """Execute fades and wait until all fades for given channels complete."""
    f()
    asyncio.gather(*[ch.wait_till_fade_complete() for ch in chs])


async def main():
    node = ArtNetNode("192.168.31.9")
    # node = ArtNetNode('255.255.255.255', broadcast=True)
    await node.start()

    ## Define channels

    universe = node.add_universe(0)

    flood_master = universe.add_channel(18, width=1)
    flood_r = universe.add_channel(19, width=1)
    flood_g = universe.add_channel(20, width=1)
    flood_b = universe.add_channeol(21, width=1)

    ## More concurrent fades
               
    def reset():
        flood_r.add_fade([0], 0)
        flood_g.add_fade([0], 0)
        flood_b.add_fade([0], 0)

    await wait([flood_r, flood_g, flood_b], reset)

    # you can inline reset()

    await wait([flood_r, flood_g, flood_b],
               lambda: (flood_r.add_fade([0], 0),
                        flood_g.add_fade([0], 0),
                        flood_b.add_fade([0], 0)))
               
    # TaskGroup showcase

    async with asyncio.TaskGroup() as tg:

        async def r_then_g_then_b():
            await fade(flood_r, [255], 1000)

            await fade(flood_r, [0], 1000)
            await fade(flood_g, [255], 1000)

            await fade(flood_g, [0], 1000)
            await fade(flood_b, [255], 1000)

        async def master_wobble():
            for i in range(10):
                await fade(flood_master, [80], 500)
                await fade(flood_master, [100], 500)

        tg.create_task(r_then_g_then_b())
        tg.create_task(master_wobble())


asyncio.run(main())
