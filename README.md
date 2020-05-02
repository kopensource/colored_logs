# colored_logs ![Python 3.6](https://img.shields.io/static/v1?label=Python&message=3.6%20|%203.7&color=blue)

### Install
```Bash
pip install install colored-logs
```
or
```Bash
pip3 install install colored-logs
```

### Features
* __Print different types of logs__ _(info, success, fail, warning, error, subtle)_
* __Add custom color for each type of log__ _(override default values)_
* __Mark logs with custom ids__ _(optional, defaults to no id)_
* __Show type for every log__ _(optional, defaults to True)_
* __Show time of logging for every log__ _(optional, defaults to True)_
* __Log async task__

### Usage
```Python
import time

from colored_logs import logger

log = logger.Logger(id='Test-id-1')

log.info('This is an info log')
time.sleep(0.5)

log.id='Test-id-2'
log.info('This is an info log with a new id')
log.id='Test-id-1'
time.sleep(0.5)

log.success('This is a success log')
time.sleep(0.5)
log.warning('This is a warning log')
time.sleep(0.5)
log.error('This is an error log')
time.sleep(0.5)
log.fail('This is a fail log')

time.sleep(1)

log.start_process('This is taking a while')
time.sleep(3.5)
log.info('This is an info log while also logging the active process')

time.sleep(3.5)

duration_float_seconds = log.stop_process(
    log_type=logger.LogType.Success,
    values='Successfully finished task'
)
```

### In action
![screenshot](https://v.redd.it/ukunwf7xcdw41/DASH_720?source=fallback)

### Credit
This package relies on [colored](https://pypi.org/project/colored/), which is maintained by [dslackw](https://pypi.org/user/dslackw/)
