import asyncio
from pyartnet import ArtNetNode


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

    ## Simple fades

    flood_master.add_fade([255], 0)
    await flood_master.wait_till_fade_complete()

    flood_r.add_fade([255], 1000)
    await flood_r.wait_till_fade_complete()


asyncio.run(main())
