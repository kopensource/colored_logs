from typing import List, Optional, Union
from threading import Lock, Thread
import time

from .utils import LoggerUtils

from .models.color import Color
from .models.color_pair import ColorPair
from .models.color_config import ColorConfig

from .models.log_type import LogType
from .models.icon_set import IconSet
from .models.log_info import LogInfo
from .models.animation_type import AnimationType
from .models.log_environment import LogEnvironment


class Logger:
    def __init__(
        self,
        color_config: ColorConfig = ColorConfig(),
        icon_set: IconSet = IconSet(),
        log_structure: Optional[List[LogInfo]] = None,
        animation_type: AnimationType = AnimationType.Dots,
        animation_sleep: float = 0.5,
        loginfo_id_len: int = 14,
        ID: Optional[str] = None,
        environment: LogEnvironment = LogEnvironment.Console,
        console_line_char_len: Optional[int] = None
    ):
        self.color_config = color_config
        self.icon_set = icon_set
        self.log_structure = log_structure or [LogInfo.LogType, LogInfo.ID, LogInfo.Icon, LogInfo.Message, LogInfo.Time]
        self.animation_type = animation_type
        self.animation_sleep = animation_sleep
        self.ID = ID
        self.environment = environment
        self.console_line_char_len = console_line_char_len
        self.loginfo_id_len = loginfo_id_len

        self.lock = Lock()
        self.utils = LoggerUtils()

        self.__process_thread = None
        self.__thread_start_time = None
        self.__thread_working = False
        self.__thread_lock = Lock()

    def info(
        self,
        *values: object,
        ID: Optional[str] = None,
        color: Optional[Union[str, Color, ColorPair]] = None,
        dim_color: Optional[Union[str, Color, ColorPair]] = None,
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
        color: Optional[Union[str, Color, ColorPair]] = None,
        dim_color: Optional[Union[str, Color, ColorPair]] = None,
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
        color: Optional[Union[str, Color, ColorPair]] = None,
        dim_color: Optional[Union[str, Color, ColorPair]] = None,
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
        color: Optional[Union[str, Color, ColorPair]] = None,
        dim_color: Optional[Union[str, Color, ColorPair]] = None,
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
        color: Optional[Union[str, Color, ColorPair]] = None,
        dim_color: Optional[Union[str, Color, ColorPair]] = None,
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
        color: Optional[Union[str, Color, ColorPair]] = None,
        dim_color: Optional[Union[str, Color, ColorPair]] = None,
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
        *values: object,
        color: Optional[Union[str, Color, ColorPair]] = None
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
        log_type: LogType,
        *values: object,
        ID: Optional[str] = None,
        color: Optional[Union[str, Color, ColorPair]] = None,
        dim_color: Optional[Union[str, Color, ColorPair]] = None,
        icon: Optional[str] = None,
        log_structure: Optional[List[LogInfo]] = None,
        animation_type: Optional[AnimationType] = None,
        animation_sleep: Optional[float] = None
    ) -> None:
        if log_type in [LogType.Info, LogType.Success, LogType.Fail, LogType.Error]:
            log_func = self.info

            if log_type == LogType.Success:
                log_func = self.success
            elif log_type == LogType.Fail:
                log_func = self.fail
            elif log_type == LogType.Error:
                log_func = self.error
            
            log_func(*values, ID=ID, color=color, dim_color=dim_color, icon=icon, log_structure=log_structure)
        elif log_type == LogType.Subtle:
            self.subtle(*values, color=color)
        elif log_type == LogType.Process:
            self.start_process(*values, ID=ID, color=color, dim_color=dim_color, icon=icon, log_structure=log_structure, animation_type=animation_type, animation_sleep=animation_sleep)
    
    def start_process(
        self,
        *values: object,
        ID: Optional[str] = None,
        color: Optional[Union[str, Color, ColorPair]] = None,
        dim_color: Optional[Union[str, Color, ColorPair]] = None,
        icon: Optional[str] = None,
        log_structure: Optional[List[LogInfo]] = None,
        animation_type: Optional[AnimationType] = None,
        animation_sleep: Optional[float] = None
    ) -> None:
        self.stop_process()
        self.__thread_working = True
        self.__process_thread = Thread(
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

        self.__thread_start_time = time.time()
        self.__process_thread.start()
    
    def stop_process(
        self,
        log_type: Optional[LogType] = None,
        values: object = None,
        ID: Optional[str] = None,
        color: Optional[Union[str, Color, ColorPair]] = None,
        dim_color: Optional[Union[str, Color, ColorPair]] = None,
        icon: Optional[str] = None,
        log_structure: Optional[List[LogInfo]] = None,
        animation_type: Optional[AnimationType] = None,
        animation_sleep: Optional[float] = None
    ) -> Optional[float]:
        duration_s = None
        
        if self.__process_thread is not None:
            self.__thread_lock.acquire()
            try:
                self.__thread_working = False
            finally:
                self.__thread_lock.release()

            self.__process_thread.join()
            self.__process_thread = None
            duration_s = time.time() - self.__thread_start_time
        else:
            return None

        if log_type is not None and values is not None and duration_s is not None:
            if not isinstance(values, tuple):
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
        color: Optional[Union[str, Color, ColorPair]],
        dim_color: Optional[Union[str, Color, ColorPair]],
        icon: Optional[str],
        log_structure: List[LogInfo],
        log_type: Optional[str],
        animation_type: AnimationType,
        animation_sleep: float
    ) -> None:        
        start_time = time.time()
        i = 0

        while True:
            self.__thread_lock.acquire()
            try:
                if not self.__thread_working:
                    return
            finally:
                self.__thread_lock.release()

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
        main_color: Optional[Union[str, Color, ColorPair]],
        dim_color: Optional[Union[str, Color, ColorPair]],
        prefix: str = '',
        icon: Optional[str] = None,
        log_structure: Optional[List[LogInfo]] = None,
        log_type: Optional[str] = None,
        message_separator: str = ' ',
        component_separator: str = ' | ',
        end: Optional[str] = None
    ) -> None:
        import inspect
        
        self.lock.acquire()
        try:
            self.__log_sync(
                values,
                prefix,
                ID,
                main_color,
                dim_color,
                icon,
                log_type or inspect.currentframe().f_back.f_code.co_name,
                log_structure or [LogInfo.Message],
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
        main_color: Optional[Union[str, Color, ColorPair]],
        dim_color: Optional[Union[str, Color, ColorPair]],
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
                    log_component = self.utils.uniform_len_string(ID, self.loginfo_id_len)
            elif log_info == LogInfo.Message:
                if len(message) > 0:
                    log_component = message

            if log_component is not None:
                log_components.append(self.utils.styled_string(log_component, log_info, main_color, dim_color, self.environment))

        message = self.utils.styled_string(component_separator, LogInfo.Time, main_color, dim_color, self.environment).join(log_components)

        if LogInfo.Time in log_structure:
            time_str = self.utils.time_str_hour_format()
            time_icon = self.icon_set.time

            if time_icon is not None and len(time_icon) > 0:
                time_str = time_icon + ' ' + time_str

            message = self.utils.append_to_string_to_console_edge(
                message,
                self.utils.styled_string(time_str, LogInfo.Time, main_color, dim_color, self.environment),
                self.environment,
                console_line_char_len=self.console_line_char_len
            )
        else:
            message = self.utils.append_to_string_to_console_edge(message, '', self.environment, console_line_char_len=self.console_line_char_len)

        if self.environment == LogEnvironment.HTML:
            message = '<pre>' + message + '</pre>'

        print(prefix+message, end=end)