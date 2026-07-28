"""
Logging Configuration
=====================
Centralized logging configuration that can be imported by any module.
"""
import logging
import sys

def setup_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        # Create console handler with a higher log level
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.INFO)

        # Create file handler which logs even debug messages
        fh = logging.FileHandler('app.log')
        fh.setLevel(logging.DEBUG)

        # Create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)

        # Add the handlers to the logger
        logger.addHandler(ch)
        logger.addHandler(fh)

    return logger

# Example usage
if __name__ == "__main__":
    logger = setup_logger(__name__)
    logger.debug("This is a debug message (goes to file only)")
    logger.info("This is an info message (goes to console and file)")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
