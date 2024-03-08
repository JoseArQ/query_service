import logging

def get_stream_logger(*, name : str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    stream_formatter = logging.Formatter('%(levelname)s - function: %(funcName)% - %(message)s')

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(stream_formatter)

    logger.addHandler(stream_handler)
    return logger