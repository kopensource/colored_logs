# colored_logs ![Python 3.6](https://img.shields.io/static/v1?label=Python&message=3.6%20|%203.7&color=blue)

### Install
```Bash
pip install install colored-logs==0.0.2
```
or
```Bash
pip3 install install colored-logs==0.0.2
```

### Features
* __Print different types of logs__         _(info, success, warning, error, subtle)_
* __Add custom color for each type of log__ _(override defauld values)_
* __Mark logs with custom ids__             _(optional, defaults to no id)_
* __Show type for every log__               _(optional, defaults to True)_
* __Show time of logging for every log__    _(optional, defaults to True)_

### Usage
```Python
from colored_logs.logger import Logger

log = Logger(id='Test-id-1')
log.info('This is an info log')
log.success('This is a success log')
log.warning('This is a warning log')
log.error('This is an error log')
log.subtle('This is a subtle log')

log.set_id('Test-id-2')
log.info('This a log with a new id')

log.set_id('shortened-long_id-2')
log.info('This a log with a long id')

log.set_id(None)
log.info('This a log with no id')

log.set_print_log_type(False)
log.info('This a log with no log type')

log.set_print_time(False)
log.info('This a log with no time')
```

### In action
![screenshot](https://i.imgur.com/PERVCo4.png)

### Credit
This package relies on [colored](https://pypi.org/project/colored/), which is maintained by [dslackw](https://pypi.org/user/dslackw/)
