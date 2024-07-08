from concretehandler import ErrorLogger, DebugLogger, InfoLogger
from abstracthandler import Logger

def get_chain_of_loggers():
    error_logger = ErrorLogger(Logger.ERROR)
    debug_logger = DebugLogger(Logger.DEBUG)
    info_logger = InfoLogger(Logger.INFO)

    error_logger.set_next_logger(debug_logger)
    debug_logger.set_next_logger(info_logger)

    return error_logger
