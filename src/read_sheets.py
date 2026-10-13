import os

import pandas as pd


def read_csv(
    path: str = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "transactions.csv")
) -> list[dict]:
    """Функция для чтения csv файлов"""
    if not os.path.exists(path):
        raise FileNotFoundError("Файл не найден")
    if not os.path.isfile(path):
        raise ValueError("Объект является директорией")
    if not path.endswith(".csv"):
        raise ValueError("Расширение файла не является csv")
    reader = pd.read_csv(path, delimiter=";")
    return reader.to_dict("records")


def read_xlsx(
    path: str = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "transactions_excel.xlsx"
    )
) -> list[dict]:
    """Функция для чтения xlsx файлов"""
    if not os.path.exists(path):
        raise FileNotFoundError("Файл не найден")
    if not os.path.isfile(path):
        raise ValueError("Объект является директорией")
    if not path.endswith(".xlsx"):
        raise ValueError("Расширение файла не является xlsx")
    reader = pd.read_excel(path)
    return reader.to_dict("records")
