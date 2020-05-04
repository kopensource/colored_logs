class Color:
    def __init__(
        self,
        r: int,
        g: int,
        b: int,
    ):
        self.validate(r, g, b)

        self.r = r
        self.g = g
        self.b = b
    
    @staticmethod
    def validate(
        r: int,
        g: int,
        b: int,
    ):
        for i in [r, g, b]:
            if i < 0 or i > 255:
                raise Exception('Could not validate color:' + ' r:'+str(r) + ' g:'+str(g) + ' b:'+str(b))
    
    @classmethod
    def fromHex(
        cls,
        hex_str: str
    ):
        r, g, b = tuple(int(hex_str.strip('#')[i:i+2], 16) for i in (0, 2, 4))

        return cls(r, g, b)
    
    @classmethod
    def fromHSV(
        cls,
        h: float,
        s: float,
        v: float,
        h_range: int = 360,
        s_range: int = 100,
        v_range: int = 100,
    ):
        import colorsys

        h /= float(h_range)
        s /= float(s_range)
        v /= float(v_range)

        r, g, b = tuple(round(i * 255.0) for i in colorsys.hsv_to_rgb(h,s,v))

        return cls(r, g, b)
    
    @classmethod
    def fromHSL(
        cls,
        h: float,
        s: float,
        l: float,
        h_range: int = 360,
        s_range: int = 100,
        l_range: int = 100,
    ):
        import colorsys

        h /= float(h_range)
        s /= float(s_range)
        l /= float(l_range)

        r, g, b = tuple(round(i * 255.0) for i in colorsys.hls_to_rgb(h,l,s))

        return cls(r, g, b)
    
    @classmethod
    def fromCMYK(
        cls,
        c: float,
        m: float,
        y: float,
        k: float,
        cmyk_scale: int = 100
    ):
        r, g, b = tuple(round(255.0 * (1.0 - i / float(cmyk_scale)) * (1.0 - k / float(cmyk_scale))) for i in (c, m, y))

        return cls(r, g, b) 