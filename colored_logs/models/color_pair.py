from typing import Optional, Union

from .color import Color

class ColorPair:
    def __init__(
        self,
        foreground: Optional[Union[str, Color]] = None,
        background: Optional[Union[str, Color]] = None,
    ):
        if foreground is None and background is None:
            raise 'You need to specify at least 1 color for a ColorPair'

        self.foreground = self.__color(foreground)
        self.background = self.__color(background)

    def __color(
        self,
        color: Optional[Union[str, Color]]
    ) -> Optional[ColorPair]:
        if not color:
            return None

        return color if isinstance(color, Color) else Color.fromHex(color)