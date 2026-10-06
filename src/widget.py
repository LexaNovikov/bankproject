import logging
from logging import DEBUG

from .masks import get_mask_account, get_mask_card_number

root_logger = logging.getLogger()
widget_logger = logging.getLogger("masks")
widget_handler = logging.FileHandler("../logs/masks.log", mode="w")
widget_formater = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
widget_handler.setFormatter(widget_formater)
widget_logger.addHandler(widget_handler)
widget_logger.setLevel(DEBUG)


def mask_account_card(card_number_or_account: str) -> str:
    """Функция для определения и маскировки карт и аккаунтов"""
    data = card_number_or_account.split()
    if len(data) == 0 or len(data[-1]) == 0:
        widget_logger.debug("Некорректный номер счета или карты")
        raise ValueError("Некорректный номер счета или карты")
    for char in data[-1]:
        if char not in "1234567890":
            widget_logger.debug("Некорректный номер счета или карты")
            raise ValueError("Некорректный номер счета или карты")
    if len(data[-1]) == 16:
        masked_card_number = get_mask_card_number(data[-1])
        data[-1] = masked_card_number
        return " ".join(data)
    elif len(data[-1]) == 20:
        masked_account = get_mask_account(data[-1])
        data[-1] = masked_account
        return " ".join(data)
    else:
        widget_logger.debug("Некорректный номер счета или карты")
        raise ValueError("Некорректный номер счета или карты")


mask_account_card("378192461625348")


def get_date(date: str) -> str:
    """Функция для форматирования даты"""
    raw_date = date[:10]
    if len(raw_date) == 0:
        raise ValueError("Дан некорректный формат даты или не дата вовсе")
    for idx, char in enumerate(raw_date):
        if ((idx == 4 or idx == 7) and char != "-") or ((idx != 4 and idx != 7) and char not in "0123456789"):
            raise ValueError("Дан некорректный формат даты или не дата вовсе")
    final_date = raw_date.split("-")
    final_date[0], final_date[2] = final_date[2], final_date[0]
    result = ".".join(final_date)
    return result
