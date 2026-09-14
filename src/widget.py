from masks import get_mask_account, get_mask_card_number
def mask_account_card(card_number_or_account: str) -> str:
    data = card_number_or_account.split()
    if len(data[-1]) == 16:
        masked_card_number = get_mask_card_number(data[-1])
        data [-1] = masked_card_number
        return " ".join(data)
    else:
        masked_account = get_mask_account(data[-1])
        data[-1] = masked_account
        return " ".join(data)
print(mask_account_card(input()))


