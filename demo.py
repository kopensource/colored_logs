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