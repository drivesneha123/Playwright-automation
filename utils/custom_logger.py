import logging
import os


def setup_logger(log_file="logs/dspt.log"):
    """
    Set up and return a shared logger instance for Behave tests.
    """
    logger = logging.getLogger("behave_logger")
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        # File handler
        file_handler = logging.FileHandler(log_file, mode="w")
        file_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(name)s - %(message)s"
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger


# Shared singleton logger
logger = setup_logger()
