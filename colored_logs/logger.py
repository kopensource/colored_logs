from typing import List, Optional
from threading import Lock
from multiprocessing import Process
import time

from .models import color_config as cc, icon_set as ics, log_info as li, animation_type as at, log_type as lt, log_environment as le
from .utils import LoggerUtils

ColorConfig = cc.ColorConfig
IconSet = ics.IconSet
LogInfo = li.LogInfo
AnimationType = at.AnimationType
LogType = lt.LogType
LogEnvironmeent = le.LogEnvironment

class Logger:
    def __init__(
        self,
        color_config: ColorConfig = ColorConfig(),
        icon_set: IconSet = IconSet(),
        log_structure: List[LogInfo] = [LogInfo.LogType, LogInfo.ID, LogInfo.Icon, LogInfo.Message, LogInfo.Time],
        animation_type: AnimationType = AnimationType.Dots,
        animation_sleep: float = 0.5,
        ID: Optional[str] = None,
        environment: LogEnvironmeent = LogEnvironmeent.Console,
        console_line_char_len: Optional[int] = None
    ):
        self.color_config = color_config
        self.icon_set = icon_set
        self.log_structure = log_structure
        self.animation_type = animation_type
        self.animation_sleep = animation_sleep
        self.ID = ID
        self.environment = environment
        self.console_line_char_len = console_line_char_len

        self.lock = Lock()
        self.utils = LoggerUtils()

    def info(
        self,
        *values: object,
        ID: Optional[str] = None,
        color: Optional[str] = None,
        dim_color: Optional[str] = None,
        icon: Optional[str] = None,
        log_structure: Optional[List[LogInfo]] = None
    ) -> None:
        self.__log(
            values,
            ID or self.ID,
            color or self.color_config.info,
            dim_color or self.color_config.dim,
            icon=icon or self.icon_set.info,
            log_structure=log_structure or self.log_structure
        )
    
    def success(
        self,
        *values: object,
        ID: Optional[str] = None,
        color: Optional[str] = None,
        dim_color: Optional[str] = None,
        icon: Optional[str] = None,
        log_structure: Optional[List[LogInfo]] = None
    ) -> None:
        self.__log(
            values,
            ID or self.ID,
            color or self.color_config.success,
            dim_color or self.color_config.dim,
            icon=icon or self.icon_set.success,
            log_structure=log_structure or self.log_structure
        )
    
    def fail(
        self,
        *values: object,
        ID: Optional[str] = None,
        color: Optional[str] = None,
        dim_color: Optional[str] = None,
        icon: Optional[str] = None,
        log_structure: Optional[List[LogInfo]] = None
    ) -> None:
        self.__log(
            values,
            ID or self.ID,
            color or self.color_config.fail,
            dim_color or self.color_config.dim,
            icon=icon or self.icon_set.fail,
            log_structure=log_structure or self.log_structure
        )
    
    def warning(
        self,
        *values: object,
        ID: Optional[str] = None,
        color: Optional[str] = None,
        dim_color: Optional[str] = None,
        icon: Optional[str] = None,
        log_structure: Optional[List[LogInfo]] = None
    ) -> None:
        self.__log(
            values,
            ID or self.ID,
            color or self.color_config.warning,
            dim_color or self.color_config.dim,
            icon=icon or self.icon_set.error,
            log_structure=log_structure or self.log_structure
        )
    
    def error(
        self,
        *values: object,
        ID: Optional[str] = None,
        color: Optional[str] = None,
        dim_color: Optional[str] = None,
        icon: Optional[str] = None,
        log_structure: Optional[List[LogInfo]] = None
    ) -> None:
        self.__log(
            values,
            ID or self.ID,
            color or self.color_config.error,
            dim_color or self.color_config.dim,
            icon=icon or self.icon_set.error,
            log_structure=log_structure or self.log_structure
        )
    
    def critical(
        self,
        *values: object,
        ID: Optional[str] = None,
        color: Optional[str] = None,
        dim_color: Optional[str] = None,
        icon: Optional[str] = None,
        log_structure: Optional[List[LogInfo]] = None
    ) -> None:
        self.__log(
            values,
            ID or self.ID,
            color or self.color_config.critical,
            dim_color or self.color_config.dim,
            icon=icon or self.icon_set.critical,
            log_structure=log_structure or self.log_structure
        )
    
    def subtle(
        self,
        color: Optional[str] = None,
        *values: object
    ) -> None:
        self.__log(
            values,
            None,
            color or self.color_config.info,
            self.color_config.dim,
            log_structure=[LogInfo.Message]
        )
    
    def log(
        self,
        type: LogType,
        *values: object,
        ID: Optional[str] = None,
        color: Optional[str] = None,
        dim_color: Optional[str] = None,
        icon: Optional[str] = None,
        log_structure: Optional[List[LogInfo]] = None,
        animation_type: Optional[AnimationType] = None,
        animation_sleep: Optional[float] = None
    ) -> None:
        if type in [LogType.Info, LogType.Success, LogType.Fail, LogType.Error]:
            log_func = self.info

            if type == LogType.Success:
                log_func = self.success
            elif type == LogType.Fail:
                log_func = self.fail
            elif type == LogType.Error:
                log_func = self.error
            
            log_func(*values, ID=ID, color=color, dim_color=dim_color, icon=icon, log_structure=log_structure)
        elif type == LogType.Subtle:
            self.subtle(*values, color=color)
        elif type == LogType.Process:
            self.start_process(*values, ID=ID, color=color, dim_color=dim_color, icon=icon, log_structure=log_structure, animation_type=animation_type, animation_sleep=animation_sleep)
    
    def start_process(
        self,
        *values: object,
        ID: Optional[str] = None,
        color: Optional[str] = None,
        dim_color: Optional[str] = None,
        icon: Optional[str] = None,
        log_structure: Optional[List[LogInfo]] = None,
        animation_type: Optional[AnimationType] = None,
        animation_sleep: Optional[float] = None
    ) -> None:
        self.stop_process()
        self.process = Process(
            target=self.__process,
            args=(
                values,
                ID or self.ID,
                color or self.color_config.process,
                dim_color or self.color_config.dim,
                icon or self.icon_set.process,
                log_structure or self.log_structure,
                'process',
                animation_type or self.animation_type,
                animation_sleep or self.animation_sleep
            )
        )

        self.process_start_time = time.time()
        self.process.start()
    
    def stop_process(
        self,
        log_type: Optional[LogType] = None,
        values: object = None,
        ID: Optional[str] = None,
        color: Optional[str] = None,
        dim_color: Optional[str] = None,
        icon: Optional[str] = None,
        log_structure: Optional[List[LogInfo]] = None,
        animation_type: Optional[AnimationType] = None,
        animation_sleep: Optional[float] = None
    ) -> Optional[float]:
        duration_s = None
        
        try:
            self.process.terminate()
            self.process = None

            duration_s = time.time() - self.process_start_time
        except:
            pass

        if log_type is not None and values is not None and duration_s is not None:
            if type(values) != tuple:
                values = (values,)
            
            values +=  (self.utils.duration_str(duration_s),)

            self.log(
                log_type, *values,
                ID=ID,
                color=color,
                dim_color=dim_color,
                icon=icon,
                log_structure=log_structure,
                animation_type=animation_type,
                animation_sleep=animation_sleep
            )
        
        return duration_s
    

    # PRIVATE

    def __process(
        self,
        values: object,
        ID: Optional[str],
        color: Optional[str],
        dim_color: Optional[str],
        icon: Optional[str],
        log_structure: List[LogInfo],
        log_type: Optional[str],
        animation_type: AnimationType,
        animation_sleep: float
    ) -> None:        
        start_time = time.time()
        i = 0

        while True:
            diff_s = int(time.time() - start_time)
            animation_str = animation_type.value[i%len(animation_type.value)]
            time_str = time.strftime('%H:%M:%S', time.gmtime(diff_s))

            self.__log(
                (animation_str,) + values + (time_str,),
                ID,
                color,
                dim_color,
                prefix='',
                icon=icon,
                log_structure=log_structure,
                log_type=log_type,
                end='\r'
            )

            i += 1
            time.sleep(animation_sleep)

    def __log(
        self,
        values: object,
        ID: Optional[str],
        main_color_hex: str,
        dim_color_hex: str,
        prefix: str = '',
        icon: Optional[str] = None,
        log_structure: List[LogInfo] = [LogInfo.Message],
        log_type: Optional[str] = None,
        message_separator: str = ' ',
        component_separator: str = ' | ',
        end: Optional[str] = None
    ) -> None:
        import inspect

        try:
            log_type = log_type or inspect.stack()[1][3]
        except:
            pass

        self.lock.acquire()
        try:
            self.__log_sync(
                values,
                prefix,
                ID,
                main_color_hex,
                dim_color_hex,
                icon,
                log_type,
                log_structure,
                message_separator,
                component_separator,
                end
            )
        finally:
            self.lock.release()

    def __log_sync(
        self,
        values: object,
        prefix: str,
        ID: str,
        main_color_hex: str,
        dim_color_hex: str,
        icon: Optional[str],
        log_type: Optional[str],
        log_structure: List[LogInfo],
        message_separator: str,
        component_separator: str,
        end: Optional[str]
    ) -> None:
        if LogInfo.Icon in log_structure and icon is not None and len(icon) > 0:
            values = (icon,) + values

        message = ''

        for value in values:
            if len(message) > 0:
                message += message_separator
            
            message += str(value)

        log_components = []
        
        for log_info in log_structure:
            log_component = None

            if log_info == LogInfo.LogType:
                if log_type is not None:
                    log_component = self.utils.uniform_len_string(log_type.upper(), 8)
            elif log_info == LogInfo.ThreadName:
                import threading

                log_component = self.utils.uniform_len_string(threading.current_thread().getName(), 10)
            elif log_info == LogInfo.ID:
                if ID is not None and len(ID) > 0:
                    log_component = self.utils.uniform_len_string(ID, 14)
            elif log_info == LogInfo.Message:
                if len(message) > 0:
                    log_component = message
            
            if log_component is not None:
                log_components.append(self.utils.styled_string(log_component, log_info, main_color_hex, dim_color_hex, self.environment))
        
        message = self.utils.styled_string(component_separator, LogInfo.Time, main_color_hex, dim_color_hex, self.environment).join(log_components)

        if LogInfo.Time in log_structure:
            time_str = self.utils.time_str_hour_format()
            time_icon = self.icon_set.time

            if time_icon is not None and len(time_icon) > 0:
                time_str = time_icon + ' ' + time_str
            
            message = self.utils.append_to_string_to_console_edge(
                message,
                self.utils.styled_string(time_str, LogInfo.Time, main_color_hex, dim_color_hex, self.environment),
                self.environment,
                console_line_char_len=self.console_line_char_len
            )
        else:
            message = self.utils.append_to_string_to_console_edge(message, '', self.environment, console_line_char_len=self.console_line_char_len)

        if self.environment == LogEnvironmeent.HTML:
            message = '<pre>' + message + '</pre>'

        print(prefix+message, end=end)