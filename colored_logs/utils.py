from .models.log_info import LogInfo

class LoggerUtils:
    def styled_string(
        self,
        message: str,
        log_info: LogInfo,
        main_color: str,
        dim_color: str
    ) -> str:
        from colored import style, fg

        color = dim_color

        if log_info in [LogInfo.LogType, LogInfo.Icon, LogInfo.Message]:
            color = main_color

        return style.BOLD + fg(self.hex(color)) + message + style.RESET

    def hex(
        self,
        hex_str: str
    ) -> str:
        if not hex_str.startswith('#'):
            hex_str = '#' + hex_str
        
        return hex_str

    def uniform_len_string(
        self,
        string: str,
        preferred_length: int = 8,
        filling_char: str = ' '
    ) -> str:
        while len(string) < preferred_length:
            string += filling_char
        
        if len(string) > preferred_length:
            string = string[:preferred_length-1] + '.'
        
        return string

    def append_to_string_to_console_edge(
        self,
        string: str,
        string_to_append: str,
        filler_char: str = ' ',
    ) -> str:
        max_console_len = self.console_max_chars_per_line()
        unescaped_string = self.string_without_ansii(string)
        unescaped_string_to_append = self.string_without_ansii(string_to_append)

        available_length = max_console_len - len(unescaped_string) - len(unescaped_string_to_append) - 1

        if available_length >= 0:
            return string + ' ' * available_length + string_to_append
        
        return unescaped_string

    def time_str_hour_format(self) -> str:
        import time

        return time.strftime("%H:%M:%S", time.localtime())
    
    def duration_str(self, seconds: float) -> str:
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

    def console_max_chars_per_line(self) -> int:
        import os

        _, columns = os.popen('stty size', 'r').read().split()

        return int(columns)

    def string_without_ansii(
        self,
        string: str
    ) -> str:
        import re

        ansi_escape = re.compile(r'(?:\x1B[@-_]|[\x80-\x9F])[0-?]*[ -/]*[@-~]')

        return ansi_escape.sub('', string)