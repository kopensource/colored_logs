# colored_logs
![python_version](https://img.shields.io/static/v1?label=Python&message=3.5%20|%203.6%20|%203.7&color=blue) [![PyPI download month](https://img.shields.io/pypi/dm/colored-logs?logo=pypi&logoColor=white)](https://pypi.python.org/pypi/colored-logs/) [![PyPI version](https://img.shields.io/pypi/v/colored-logs?logo=pypi&logoColor=white)](https://pypi.python.org/pypi/colored-logs/) [![build](https://img.shields.io/travis/com/kopensource/colored_logs/develop?logo=travis)](https://travis-ci.com/github/kopensource/colored_logs) [![codecov](https://img.shields.io/codecov/c/gh/kopensource/colored_logs/develop?logo=codecov)](https://codecov.io/gh/kopensource/colored_logs) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/ead083cfe67f4ee7b65203ee8977d416)](https://www.codacy.com/gh/kopensource/colored_logs?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=kopensource/colored_logs&amp;utm_campaign=Badge_Grade) [![DeepSource](https://static.deepsource.io/deepsource-badge-dark-mini.svg)](https://deepsource.io/gh/kopensource/colored_logs/?ref=repository-badge)


### Install
```Bash
pip install colored-logs
```
or
```Bash
pip3 install colored-logs
```

### Features
* __Print different types of logs__ _(info, success, fail, warning, error, critical, subtle)_
* __Add custom color for each type of log__ _(both foreground and background. Defaults to these [colors](https://coolors.co/b4aea8-3ea966-c8553d-f28f3b-a22b24-f3f3f3-982720-2bc4e9-918b86))_
* __Can Provide colors in RGB, HEX, HSV, HSL, or CMYK__
* __Mark logs with custom ids__ _(optional, defaults to no id)_
* __Show type for every log__ _(optional, defaults to True)_
* __Show time of logging for every log__ _(optional, defaults to True)_
* __Change logging env to html__ _(defaults to Console. In html it appears like [this](https://jsfiddle.net/s2b4zpdq/))_
* __Log async task__

### Usage
```Python
import time

from colored_logs.logger import Logger, LogType#, LogEnvironmeent

log = Logger(
    ID='Test-id-1'
    # environment=LogEnvironmeent.HTML,  # Override to print html logs
    # console_line_char_len=90           # Optionally provide how many chars does fir in one consolee line
)

log.info('This is an info log')
time.sleep(0.5)

log.ID='Test-id-2'
log.info('This is an info log with a new id')
log.ID='Test-id-1'
time.sleep(0.5)

log.success('This is a success log')
time.sleep(0.5)
log.warning('This is a warning log')
time.sleep(0.5)
log.error('This is an error log')
time.sleep(0.5)
log.fail('This is a fail log')
time.sleep(0.5)
log.critical('This is a critical log')

time.sleep(1)

log.start_process('This will take a while')
time.sleep(3.5)
log.info('This is an info log while also logging the active process')

time.sleep(3.5)

duration_float_seconds = log.stop_process(
    log_type=LogType.Success,
    values='Successfully finished task'
)
```

### In action
![video](https://thumbs.gfycat.com/PleasingLikableGrouper-size_restricted.gif)

### Credit
This package was inspired by [colored](https://pypi.org/project/colored/), which is maintained by [dslackw](https://pypi.org/user/dslackw/)
