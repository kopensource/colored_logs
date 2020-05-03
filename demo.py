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