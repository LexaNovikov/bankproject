import pandas as pd
import os

import pytest


def read_csv(path: str = "../data/transactions.csv") -> list[dict]:
    """Функция для чтения csv файлов"""
    if not os.path.exists(path):
        raise FileNotFoundError("Файл не найден")
    if not os.path.isfile(path):
        raise ValueError("Объект является директорией")
    if not path.endswith(".csv"):
        raise ValueError("Расширение файла не является csv")
    reader = pd.read_csv(path, delimiter=";")
    print(reader.to_dict("records"))
    return reader.to_dict("records")
def read_xlsx(path: str = "../data/transactions_excel.xlsx") -> list[dict]:
    """Функция для чтения xlsx файлов"""
    if not os.path.exists(path):
        raise FileNotFoundError("Файл не найден")
    if not os.path.isfile(path):
        raise ValueError("Объект является директорией")
    if not path.endswith(".xlsx"):
        raise ValueError("Расширение файла не является xlsx")
    reader = pd.read_excel(path)
    return reader.to_dict("records")


# print()
# print(read_xlsx())