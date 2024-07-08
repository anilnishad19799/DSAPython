from abstracthandler import Logger
from setupchain import get_chain_of_loggers

if __name__ == "__main__":
    logger_chain = get_chain_of_loggers()

    logger_chain.log_message(Logger.INFO, "This is an informational message.")
    logger_chain.log_message(Logger.DEBUG, "This is a debug message.")
    logger_chain.log_message(Logger.ERROR, "This is an error message.")
