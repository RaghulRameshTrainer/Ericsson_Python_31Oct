import logging
'''
5 levels:
DEBUG       10
INFO        20
WARNING     30
ERROR       40
CRITICAL    50
'''
LOG_FORMAT="%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="output.log",level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='w')
logger=logging.getLogger()
logger.debug("Debug message")
logger.info("Info")
logger.warning("Warning Message")
logger.error("An error")
logger.critical("Critical Issue")