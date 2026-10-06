import json
import logging
from logging import DEBUG

utils_logger = logging.getLogger("utils")
utils_handler = logging.FileHandler("../logs/utils.log", mode="w")
utils_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
utils_handler.setFormatter(utils_formatter)
utils_logger.addHandler(utils_handler)
utils_logger.setLevel(DEBUG)


def get_operations_data(path: str = "../data/operations.json") -> list[str]:
    """Функция для получения списка операций"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        utils_logger.debug("Функция успешно загрузила файл")
        return list(data)
    except Exception as e:
        utils_logger.error(e)
        return []
