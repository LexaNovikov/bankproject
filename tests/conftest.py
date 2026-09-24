import pytest


@pytest.fixture
def data_filter_list() -> list[dict]:
    return [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 3, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 4, "state": "EXECUTED", "date": "2020-01-01T12:00:00"},
        {"id": 5, "state": "EXECUTED", "date": "2020-02-01T12:00:00"},
        {"id": 6, "state": "EXECUTED", "date": "2020-03-01T12:00:00"},
        {"id": 7, "state": "CANCELED", "date": "2020-01-01T12:00:00"},
        {"id": 8, "state": "CANCELED", "date": "2020-02-01T12:00:00"},
        {"id": 9, "state": "EXECUTED", "date": "2020-05-15T15:30:00"},
        {"id": 10, "state": "EXECUTED", "date": "2020-01-01T12:00:00"},
        {"id": 11, "state": "CANCELED", "date": "2020-01-02T12:00:00"},
        {"id": 12, "state": "CANCELED", "date": "2020-01-03T12:00:00"},
    ]


def generators_list() -> list[dict]:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 234452123,
            "state": "CANCELED",
            "date": "2022-03-01T23:20:05.206878",
            "operationAmount": {"amount": "1488", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 387568893,
            "state": "PROCESSING",
            "date": "2026-09-22T23:20:05.206878",
            "operationAmount": {"amount": "37", "currency": {"name": "руб.", "code": "RUB"}},
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]


def usd_case() -> list[dict]:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]


def rub_case() -> list[dict]:
    return [
        {
            "id": 234452123,
            "state": "CANCELED",
            "date": "2022-03-01T23:20:05.206878",
            "operationAmount": {"amount": "1488", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 387568893,
            "state": "PROCESSING",
            "date": "2026-09-22T23:20:05.206878",
            "operationAmount": {"amount": "37", "currency": {"name": "руб.", "code": "RUB"}},
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]


def transactions_descriptions() -> list[str]:
    return ["Перевод организации", "Перевод со счета на счет", "", ""]


def card_generator_tests() -> list[tuple]:
    return [
        (
            1,
            5,
            [
                ("0000 0000 0000 0001"),
                ("0000 0000 0000 0002"),
                ("0000 0000 0000 0003"),
                ("0000 0000 0000 0004"),
                ("0000 0000 0000 0005"),
            ],
        ),
        (
            9999999999999989,
            9999999999999999,
            [
                ("9999 9999 9999 9989"),
                ("9999 9999 9999 9990"),
                ("9999 9999 9999 9991"),
                ("9999 9999 9999 9992"),
                ("9999 9999 9999 9993"),
                ("9999 9999 9999 9994"),
                ("9999 9999 9999 9995"),
                ("9999 9999 9999 9996"),
                ("9999 9999 9999 9997"),
                ("9999 9999 9999 9998"),
                ("9999 9999 9999 9999"),
            ],
        ),
    ]
