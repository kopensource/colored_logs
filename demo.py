from colored_logs.logger import Logger

log = Logger(id='Test')
log.info('This is an info log')
log.success('This is a success log')
log.warning('This is a warning log')
log.error('This is an error log')
log.subtle('This is a subtle log')