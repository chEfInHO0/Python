import logging

logging.basicConfig(filename="teste.log", level=logging.DEBUG, filemode="w", encoding="UTF-8")

log = logging.getLogger()

log.info('INFO')
log.debug('DEBUG')

log.level