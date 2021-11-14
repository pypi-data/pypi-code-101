import logging

def _get_logger():

    # 1. 创建logger和handler
    logger = logging.getLogger("logger")
    stream_handler = logging.StreamHandler()
    # file_handler = logging.FileHandler(filename=f"{FILE_PATH_FOR_HOME}/log/test.log")

    # 2. 设置level
        # DEBUG, INFO, WARNING, ERROR, CRITICAL (分别是10, 20, 30, 40, 50)
    logger.setLevel(logging.DEBUG) # 指的是: 最低能支持什么级别的打印输出
    # logger.setLevel(logging.WARNING) # 指的是: 最低能支持什么级别的打印输出
    stream_handler.setLevel(logging.DEBUG)
    # file_handler.setLevel(logging.WARNING)

    # 3. 设置log的输出格式
    formatter = logging.Formatter("%(asctime)s [%(levelname)s]:  %(message)s") # 其他格式见上面的url
    stream_handler.setFormatter(formatter)
    # file_handler.setFormatter(formatter)

    # 4. 把handler添加进logger
    logger.addHandler(stream_handler)
    # logger.addHandler(file_handler)

    return logger

logger = _get_logger()
