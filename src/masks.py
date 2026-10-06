import logging
from logging import DEBUG

root_logger = logging.getLogger()
masks_logger = logging.getLogger("masks")
masks_handler = logging.FileHandler("../logs/masks.log", mode="w")
masks_formater = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
masks_handler.setFormatter(masks_formater)
masks_logger.addHandler(masks_handler)
masks_logger.setLevel(DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """Функция для маскировки карт"""
    masked_card_number = []
    for char_idx in range(16):
        if 6 <= char_idx <= 11:
            letter = "*"
        else:
            letter = card_number[char_idx]
        if char_idx % 4 == 0 and char_idx != 0:
            masked_card_number.append(" " + letter)
        else:
            masked_card_number.append(letter)
    masks_logger.debug("Карта успешно замаскирована")
    return "".join(masked_card_number)


def get_mask_account(account: str) -> str:
    """Функция для маскировки аккаунта"""
    masks_logger.debug("Счет успешно замаскирован")
    return "**" + account[-4:]
