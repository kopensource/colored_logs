from .color_pair import ColorPair
from .color import Color

class ColorConfig:
    def __init__(
        self,
        info: str = ColorPair(foreground=Color.fromHex('#B4AEA8')),
        success: str = ColorPair(foreground=Color.fromHex('#3EA966')),
        fail: str = ColorPair(foreground=Color.fromHex('#C8553D')),
        warning: str = ColorPair(foreground=Color.fromHex('#F28F3B')),
        error: str = ColorPair(foreground=Color.fromHex('#A22B24')),
        critical: str = ColorPair(background=Color.fromHex('#982720'), foreground=Color.fromHex('#F3F3F3')),
        process: str = ColorPair(foreground=Color.fromHex('#2BC4E9')),
        dim: str = ColorPair(foreground=Color.fromHex('#918B86'))
    ):
        self.info = info
        self.success = success
        self.fail = fail
        self.warning = warning
        self.error = error
        self.critical = critical
        self.process = process
        self.dim = dim