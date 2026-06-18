import inspect
import logging

class Logger_class:
    @staticmethod
    def get_logger():
        file_handler= logging.FileHandler("Logs\orangehrm.log")
        file_handler.setLevel(logging.INFO)
        formatter= logging.Formatter('%(asctime)s - %(name)s -%(funcName)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger = logging.getLogger(inspect.stack()[1][3])
        logger.addHandler(file_handler)
        return logger
