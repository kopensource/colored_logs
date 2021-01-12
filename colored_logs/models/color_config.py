from typing import Union, Optional

from .color_pair import ColorPair
from .color import Color

class ColorConfig:
    def __init__(
        self,
        info: Union[str, Color, ColorPair] =     ColorPair(foreground='#B4AEA8'),
        success: Union[str, Color, ColorPair] =  ColorPair(foreground='#3EA966'),
        fail: Union[str, Color, ColorPair] =     ColorPair(foreground='#C8553D'),
        warning: Union[str, Color, ColorPair] =  ColorPair(foreground='#F28F3B'),
        error: Union[str, Color, ColorPair] =    ColorPair(foreground='#A22B24'),
        critical: Union[str, Color, ColorPair] = ColorPair(background='#982720', foreground='#F3F3F3'),
        process: Union[str, Color, ColorPair] =  ColorPair(foreground='#2BC4E9'),
        dim: Union[str, Color, ColorPair] =      ColorPair(foreground='#918B86')
    ):
        self.info = self._ensure_color_pair(info)
        self.success = self._ensure_color_pair(success)
        self.fail = self._ensure_color_pair(fail)
        self.warning = self._ensure_color_pair(warning)
        self.error = self._ensure_color_pair(error)
        self.critical = self._ensure_color_pair(critical)
        self.process = self._ensure_color_pair(process)
        self.dim = self._ensure_color_pair(dim)

    @staticmethod
    def _ensure_color_pair(color: Optional[Union[str, Color, ColorPair]]) -> Optional[ColorPair]:
        if not color:
            return None

        if isinstance(color, ColorPair):
            return color

        return ColorPair(foreground=color)