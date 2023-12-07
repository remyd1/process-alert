import logging

#logging.basicConfig(level = logging.INFO)
# create a new logger instead of the default root logger
logger    = logging.getLogger('process-alert')

formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

# create file handler which logs even warn messages
# info messages are displayed to stdout
logger.setLevel(logging.INFO)
fhw = logging.FileHandler('process-alert-warn.log')
fhw.setLevel(logging.WARNING)
logger.addHandler(fhw)