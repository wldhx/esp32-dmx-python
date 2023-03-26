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


class F0Laser:
    def __init__(self, universe, start: int):
        self.animation_mode = universe.add_channel(start, width=1)
        self.img_type = universe.add_channel(start + 1, width=1)
        self.rotate_cw = universe.add_channel(start + 2, width=1)
        self.rotate_xy = universe.add_channel(start + 3, width=1)
        self.rotate_z = universe.add_channel(start + 4, width=1)
        self.shift_w = universe.add_channel(start + 5, width=1)
        self.hpos = universe.add_channel(start + 6, width=1)
        self.height = universe.add_channel(start + 7, width=1)
        self.color = universe.add_channel(start + 8, width=1)


class F0Flood:
    def __init__(self, universe, start: int):
        self.master = universe.add_channel(start, width=1)
        self.r = universe.add_channel(start + 1, width=1)
        self.g = universe.add_channel(start + 2, width=1)
        self.b = universe.add_channel(start + 3, width=1)
        self.w = universe.add_channel(start + 4, width=1)
        self.amber = universe.add_channel(start + 5, width=1)
        self.violet = universe.add_channel(start + 6, width=1)
        self.strobe = universe.add_channel(start + 7, width=1)
        self.function = universe.add_channel(start + 8, width=1)
        self.function_speed = universe.add_channel(start + 9, width=1)
