import os

from .filters import process_bank_search
from .generators import filter_by_currency
from .processing import filter_by_state, sort_by_date
from .read_sheets import read_csv, read_xlsx
from .utils import get_operations_data
from .widget import get_date, mask_account_card


def waiting_valid_input(user_input: str, possible_options: list, text_to_user: str, default: None | str = None) -> str:
    """Функция, ожидающая валидный ввод пользователя"""
    if default is not None and user_input == "":
        user_input = default
    while user_input not in possible_options:
        print(f"\n{text_to_user}")
        user_input = input("Пользователь: ").upper().strip()
        if default is not None and user_input == "":
            user_input = default

    return user_input


def format_transaction(transaction: dict) -> list[str]:
    """Функция форматирования выходных данных операции"""
    result = []
    if transaction.get("date") and type(transaction.get("date")) == str:
        result.append(get_date(transaction["date"]))
    if transaction.get("description"):
        if result:
            result[0] += f" {transaction['description']}"

    if (
        transaction.get("from")
        and type(transaction.get("from")) == str
        and transaction.get("to")
        and type(transaction.get("to")) == str
    ):
        result.append(f"{mask_account_card(str(transaction["from"]))} -> {mask_account_card(str(transaction["to"]))}")
    elif type(transaction.get("to")) == str:
        result.append(mask_account_card(transaction["to"]))
    if transaction.get("amount"):
        transaction_amount = transaction["amount"]
        transaction_currency_name = transaction["currency_name"]
        result.append(f"{transaction_amount} {transaction_currency_name}")
    else:
        transaction_amount = transaction["operationAmount"].get("amount")
        transaction_currency_name = transaction["operationAmount"]["currency"]["name"]
        result.append(f"Сумма: {transaction_amount} {transaction_currency_name}")
    return result


def get_working_arr(user_input: str) -> list[dict]:
    """Функция, возвращающая изначальный список операций"""
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    match user_input:
        case "1":
            print(f"Введите путь до json файла (По умолчанию {os.path.join(base, "data", "operations.json")}): ")
            user_input = input("Пользователь: ").lower().strip()
            working_arr = get_operations_data(user_input) if user_input != "" else get_operations_data()
        case "2":
            print(f"Введите путь до csv файла (По умолчанию {os.path.join(base, "data", "transactions.csv")}): ")
            user_input = input("Пользователь: ").lower().strip()
            working_arr = read_csv(user_input) if user_input != "" else read_csv()
        case "3":
            print(f"Введите путь до xlsx файла (По умолчанию {os.path.join(base, "data", "operations_excel.xlsx")}): ")
            user_input = input("Пользователь: ").lower().strip()
            working_arr = read_xlsx(user_input) if user_input != "" else read_xlsx()
    return working_arr


def get_working_arr_after_status_filtering(working_arr: list[dict]) -> list[dict]:
    """Функция, возвращающая отфильтрованный список операций по статусу"""
    print(
        "Введите статус, по которому необходимо выполнить фильтрацию.\n"
        "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING (По умолчанию EXECUTED)"
    )
    status = waiting_valid_input(
        input("Пользователь: ").upper().strip(),
        ["EXECUTED", "CANCELED", "PENDING"],
        "Программа: Статус операции недоступен\n\n"
        "Введите статус, по которому необходимо выполнить фильтрацию.\n"
        "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING",
        "EXECUTED",
    )
    working_arr = filter_by_state(working_arr, status)
    return working_arr


def get_working_arr_after_sort_by_date(working_arr: list[dict]) -> list[dict]:
    """Функция, возвращающая отсортированный список операций по дате"""
    print("Программа: Отсортировать операции по дате? Да/Нет")
    user_input = waiting_valid_input(
        input("Пользователь: ").upper().strip(),
        ["ДА", "НЕТ"],
        "Программа: Введите 'да' или 'нет'\n\nПрограмма: Отсортировать операции по дате? Да/Нет",
    )
    if user_input == "ДА":
        print("Программа: Отсортировать по возрастанию/по убыванию? (По умолчанию: по возрастанию)")
        user_input = waiting_valid_input(
            input("Пользователь: ").upper().strip(),
            ["ПО ВОЗРАСТАНИЮ", "ПО УБЫВАНИЮ"],
            "Программа: Введите 'по взрастанию' или 'по убыванию'",
            "ПО ВОЗРАСТАНИЮ",
        )
        if user_input == "ПО ВОЗРАСТАНИЮ":
            working_arr = sort_by_date(working_arr)
        else:
            working_arr = sort_by_date(working_arr, False)
    return working_arr


def get_working_arr_after_filter_by_currency(working_arr: list[dict]) -> list[dict]:
    """Функция, возвращающая отфильтрованный список операций по валюте"""
    print("Программа: Выводить только рублевые транзакции? Да/Нет")
    user_input = waiting_valid_input(
        input("Пользователь: ").upper().strip(),
        ["ДА", "НЕТ"],
        "Программа: Введите 'да' или 'нет'\n\nПрограмма: Выводить только рублевые транзакции? Да/Нет",
    )
    if user_input == "ДА":
        working_arr = list(filter_by_currency(working_arr, "RUB"))
    return working_arr


def get_working_arr_after_description_filtering(working_arr: list[dict]) -> list[dict]:
    """Функция, возвращающая отфильтрованный список по слову в описании"""
    print("Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    user_input = waiting_valid_input(
        input("Пользователь: ").upper().strip(),
        ["ДА", "НЕТ"],
        "Программа: Введите 'да' или 'нет'\n\n"
        "Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет",
    )
    if user_input == "ДА":
        print("Программа: Введите слово")
        user_input = input("Пользователь: ")
        working_arr = process_bank_search(working_arr, user_input)
    return working_arr


def send_ans(working_arr: list) -> None:
    """Функция, выводящая список операций после всех фильтраций в консоль"""
    if len(working_arr) == 0:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации\n")
    else:
        print(
            f"Программа: Распечатываю итоговый список транзакций...\n\n"
            f"Программа: \n"
            f"Всего банковских операций в выборке: {len(working_arr)}\n"
        )
    for transaction in working_arr:
        print(*format_transaction(transaction), sep="\n", end="\n\n")


def main() -> None:
    """Основная функция проекта"""
    while True:
        print(
            "Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
            "Выберите необходимый пункт меню:\n1. Получить информацию о транзакциях из JSON-файла\n"
            "2. Получить информацию о транзакциях из CSV-файла\n"
            "3. Получить информацию о транзакциях из XLSX-файла"
        )
        user_input = input("Пользователь: ").lower().strip()
        working_arr = get_working_arr(user_input)
        working_arr_after_status_filtering = get_working_arr_after_status_filtering(working_arr)
        working_arr_after_sort_by_date = get_working_arr_after_sort_by_date(working_arr_after_status_filtering)
        working_arr_after_filter_by_currency = get_working_arr_after_filter_by_currency(working_arr_after_sort_by_date)
        working_arr_after_description_filtering = get_working_arr_after_description_filtering(
            working_arr_after_filter_by_currency
        )
        send_ans(working_arr_after_description_filtering)


if __name__ == "__main__":
    main()
