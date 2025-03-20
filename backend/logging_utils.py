import logging

def setup_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler("my_app.log")
    logger.addHandler(file_handler)
    return logger