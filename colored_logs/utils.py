from typing import Optional

from .models.color_config import ColorConfig
from .models.log_info import LogInfo
from .models.color_pair import ColorPair
from .models.color import Color
from .models.log_environment import LogEnvironment

class LoggerUtils:
    def styled_string(
        self,
        message: str,
        log_info: LogInfo,
        main_color_pair: Optional[ColorPair],
        dim_color_pair: Optional[ColorPair],
        environment: LogEnvironment
    ) -> str:
        main_color_pair = ColorConfig._ensure_color_pair(main_color_pair)
        dim_color_pair = ColorConfig._ensure_color_pair(dim_color_pair)

        color_pair = dim_color_pair

        if log_info in [LogInfo.LogType, LogInfo.Icon, LogInfo.Message]:
            color_pair = main_color_pair
        
        if environment == LogEnvironment.Console:
            return ANSI.styled(message, color_pair, self.trimmed_string_comps)
        
        return HTML.styled(message, color_pair, self.trimmed_string_comps)

    def append_to_string_to_console_edge(
        self,
        string: str,
        string_to_append: str,
        environment: LogEnvironment,
        filler_char: str = ' ',
        console_line_char_len: Optional[int] = None
    ) -> str:
        max_console_len = console_line_char_len or self.console_max_chars_per_line()

        if environment == LogEnvironment.Console:
            unescaped_string = self.string_without_ansii(string)
            unescaped_string_to_append = self.string_without_ansii(string_to_append)
        else:
            unescaped_string = self.string_without_html_tags(string)
            unescaped_string_to_append = self.string_without_html_tags(string_to_append)

        available_length = max_console_len - len(unescaped_string) - len(unescaped_string_to_append) - 1

        if available_length >= 0:
            return string + filler_char * int(float(available_length) / float(len(filler_char))) + string_to_append
        
        return unescaped_string
    
    @staticmethod
    def uniform_len_string(
        string: str,
        preferred_length: int = 8,
        filling_char: str = ' '
    ) -> str:
        while len(string) < preferred_length:
            string += filling_char
        
        if len(string) > preferred_length:
            string = string[:preferred_length-1] + '.'
        
        return string
    
    @staticmethod
    def time_str_hour_format() -> str:
        import time

        return time.strftime("%H:%M:%S", time.localtime())
    
    @staticmethod
    def duration_str(seconds: float) -> str:
        seconds = int(seconds)
        
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        
        duration = ''

        if h > 0:
            duration += str(h) + 'h'
        
        if m > 0:
            if len(duration) > 0:
                duration += ' '
                
            duration += str(m) + 'm'
        
        if s > 0:
            if len(duration) > 0:
                duration += ' '
                
            duration += str(s) + 's'

        return '~' + duration

    @staticmethod
    def console_max_chars_per_line(
        default_value: int = 80
    ) -> int:
        try:
            import os

            return os.get_terminal_size().columns
        except:
            try:
                import shutil

                return shutil.get_terminal_size(fallback=(default_value, 24))[0]
            except:
                return default_value
    
    @staticmethod
    def string_without_ansii(string: str) -> str:
        import re

        ansi_escape = re.compile(r'(?:\x1B[@-_]|[\x80-\x9F])[0-?]*[ -/]*[@-~]')

        return ansi_escape.sub('', string)
    
    @staticmethod
    def string_without_html_tags(string: str) -> str:
        _string = ''
        should_add = True

        for c in string:
            s = str(c)

            if s == '<':
                should_add = False
            elif s == '>':
                should_add = True
            elif should_add:
                _string += s
        
        return _string
    
    @staticmethod
    def trimmed_string_comps(string: str) -> (str, str, str):
        no_prefix = string.lstrip()
        no_suffix = string.rstrip()

        return string[0:len(string)-len(no_prefix)], string.strip(), string[len(no_suffix):len(string)]

class ANSI:
    @classmethod
    def styled(
        cls,
        string: str,
        color_pair: ColorPair,
        trimmed_string_comps_func,
        bold: bool = True,
        reset: bool = True
    ) -> str:
        pre, string, suf = trimmed_string_comps_func(string)
        styled_str = ''

        if bold:
            styled_str += cls.__BOLD
                
        if color_pair.foreground is not None:
            styled_str += cls.__foreground_color(color_pair.foreground)
                
        if color_pair.background is not None:
            styled_str += cls.__background_color(color_pair.background)
        
        styled_str += string

        if reset:
            styled_str += cls.__RESET
           
        return pre + styled_str + suf


    # Private

    __BOLD  = '\033[1m'.strip()
    __RESET = '\033[0m'

    @classmethod
    def __foreground_color(cls, color: Color) -> str:
        return cls.__color(color, cls.__ColorType.Foreground)
    
    @classmethod
    def __background_color(cls, color: Color) -> str:
        return cls.__color(color, cls.__ColorType.Background)
    
    from enum import Enum
    class __ColorType(Enum):
        Foreground = 38
        Background = 48
    
    @staticmethod
    def __color(
        color: Color,
        color_type: __ColorType
    ) -> str:
        return '\033[' + str(color_type.value) + ';2;' + str(color.r) + ';' + str(color.g) + ';' + str(color.b) + 'm'


class HTML:
    @classmethod
    def styled(
        cls,
        string: str,
        color_pair: ColorPair,
        trimmed_string_comps_func,
        bold: bool = True
    ) -> str:
        pre, string, suf = trimmed_string_comps_func(string)

        span_color_properties = []

        if bold:
            span_color_properties.append(cls.__BOLD)
        
        if color_pair.foreground is not None:
            span_color_properties.append(cls.__foreground_color(color_pair.foreground))
        
        if color_pair.background is not None:
            span_color_properties.append(cls.__background_color(color_pair.background))
        
        styled_str = ''

        if len(pre) > 0:
            styled_str += '<span>' + pre + '</span>'
        
        if len(string) > 0:
            styled_str += '<span style = "' + ';'.join(span_color_properties) + '">' + string + '</span>'
        
        if len(suf) > 0:
            styled_str += '<span>' + suf + '</span>'
        
        return styled_str


    # Private

    __BOLD  = 'font-weight:bold'

    @classmethod
    def __foreground_color(cls, color: Color) -> str:
        return cls.__color(color, cls.__ColorType.Foreground)
    
    @classmethod
    def __background_color(cls, color: Color) -> str:
        return cls.__color(color, cls.__ColorType.Background)
    
    from enum import Enum
    class __ColorType(Enum):
        Foreground = 'color'
        Background = 'background-color'
    
    @staticmethod
    def __color(
        color: Color,
        color_type: __ColorType
    ) -> str:
        return color_type.value + ':rgb(' + str(color.r) + ',' + str(color.g) + ',' + str(color.b) + ')'
