import logging
import os

from dotenv import load_dotenv

load_dotenv()

def setup_logger(log_file="./logs/debug.log", log_level=logging.DEBUG):
    logger = logging.getLogger("P2P")

    if logger.hasHandlers():
        return logger
    
    logger.setLevel(log_level)
    
    formatter = logging.Formatter('[%(levelname)-3s] (%(asctime)s) - (%(filename)s) -> %(name)s: %(message)s')

    console_handler = logging.StreamHandler()
    console_handler.setLevel(get_log_level())
    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(log_file, encoding=os.getenv('FORMAT'), mode='w')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


def get_log_level():
    levels = {
        "debug": logging.DEBUG,
        "info": logging.INFO,
        "warning": logging.WARNING,
        "error": logging.ERROR,
        "critical": logging.CRITICAL
    }    
    
    log_level = os.getenv("LOG_LEVEL").lower()

    if log_level in levels:
        return levels[log_level]
    else:
        raise ValueError("[!] Values for LOG_LEVEL must be either debug, info, warning, error, or critical.")
    
setup_logger()