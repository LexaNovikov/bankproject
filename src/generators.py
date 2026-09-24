from typing import Generator


def filter_by_currency(tranz_list: list[dict], currency: str) -> Generator[dict]:
    '''Функция для фильтрации словарей по валюте'''
    currency_list = list( x for x in tranz_list if x.get("operationAmount", 0) != 0 and x["operationAmount"].get("currency", 0) != 0 and x["operationAmount"]["currency"].get("code", 0) == currency)
    for currency_dict in currency_list:
        yield currency_dict


def transaction_descriptions(list_dicts: list[dict]) -> Generator[str]:
    '''Функция вывода описания транзакций'''
    for transaction in list_dicts:
        if transaction.get("description", 0) != 0:
            yield transaction["description"]
        else:
            yield ""


def card_number_generator(start: int, stop: int) -> Generator[str]:
    '''Функция генерации номера банковских карт в диапазоне'''
    if start < 1 or stop > 9999999999999999 + 1:
        raise ValueError("Начало диапазона должно быть строго больше 0, а конец диапазона меньше 9999999999999999")
    if start > stop:
        raise ValueError("Начало диапазона не должно быть больше конца диапазона")
    while start <= stop:
        raw_number = "0" * (16 - len(str(start))) + str(start)
        yield " ".join([raw_number[:4], raw_number[4:8], raw_number[8:12], raw_number[12:16]])
        start += 1
