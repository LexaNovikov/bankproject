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
    return "".join(masked_card_number)


def get_mask_account(account: str) -> str:
    """Функция для маскировки аккаунта"""
    return "**" + account[-4:]
