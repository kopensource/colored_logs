from typing import Optional
from .color import Color

class ColorPair:
    def __init__(
        self,
        foreground: Optional[Color] = None,
        background: Optional[Color] = None,
    ):
        if foreground is None and background is None:
            raise 'You need to specify at least 1 color for a ColorPair'

        self.foreground = foreground
        self.background = background