def get_mask_card_number(card_number: str) -> str:
    masked_card_number = []
    for i in range(16):
        if 6 <= i <= 11:
            letter = "*"
        else:
            letter = card_number[i]
        if i % 4 == 0 and i != 0:
            masked_card_number.append(" " + letter)
        else:
            masked_card_number.append(letter)
    return "".join(masked_card_number)


def get_mask_account(account: str) -> str:
    return "**" + account[-4:]
