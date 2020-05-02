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