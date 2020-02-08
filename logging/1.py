import logging

logging.basicConfig(filename='mylog.log', level=logging.WARNING)

logging.debug('Сообщение уровня debug:\n%s', str(globals()))
logging.info('Сообщение уровня info')
logging.warning('Сообщение уровня warning')