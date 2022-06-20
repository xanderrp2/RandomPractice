import logging
from os.path import abspath, basename, dirname, join, splitext


def BuildLogger(sourcePath):  #, logPath=None):
    srcBasename = basename(sourcePath)
    logging.basicConfig(level=logging.DEBUG)  # Must have to see DEBUG/INFO at all
    logger = logging.getLogger(srcBasename)
    logger.propagate = False  # Must remove under py3.7, but keep for earlier versions to see logger message.

    # Avoid duplicated logs caused by duplicated handlers each time we create logger from a different module.
    if logger.hasHandlers():
        return logger

    # Console log is for end-users: no debug messages.
    consoleHanlder = logging.StreamHandler()
    consoleHanlder.setLevel(logging.INFO)
    consoleHanlder.setFormatter(logging.Formatter('%(levelname)s: %(_name)s: %(message)s'))
    logger.addHandler(consoleHanlder)

    return logger

if __name__ == '__main__':
    mylogger = BuildLogger(__file__)
    mylogger.info('hello')
