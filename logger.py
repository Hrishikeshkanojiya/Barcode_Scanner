import os
import logging
from logging.handlers import RotatingFileHandler


def setup_logger():
    # Create the logs directory if it doesn't exist
    logs_dir = 'logs'
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

    # Create logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # Create formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Create file handler
    log_file = os.path.join(logs_dir, 'app.log')
    file_handler = RotatingFileHandler(log_file, maxBytes=10240, backupCount=10)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    # Add file handler to logger
    logger.addHandler(file_handler)

    return logger

