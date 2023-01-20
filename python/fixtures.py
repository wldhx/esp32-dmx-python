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
