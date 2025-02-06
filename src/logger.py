import logging
from src.config import config


def setup_logger(log_file="./logs/debug.log", log_level=logging.DEBUG):
    """
    Sets up and configures a logger for the P2P application.

    :param log_file (str): Path to the log file where logs should be stored.
    :param log_level (int): Logging level (e.g., logging.DEBUG, logging.INFO).
    
    :return: Configured logger instance.
    """
    logger = logging.getLogger("P2P")

    if logger.hasHandlers():
        return logger
    
    logger.setLevel(log_level)
    
    formatter = logging.Formatter('[%(levelname)-3s] (%(asctime)s) - (%(filename)s) -> %(name)s: %(message)s')

    console_handler = logging.StreamHandler()
    console_handler.setLevel(config.LOG_LEVEL.upper())
    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(log_file, encoding=config.FORMAT, mode='w')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger

setup_logger()