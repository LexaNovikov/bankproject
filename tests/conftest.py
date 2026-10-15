from math import nan

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


def mock_arr() -> list[dict]:
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
    ]


def csv_arr() -> list[dict]:
    return [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
        {
            "id": 3598919.0,
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "amount": 29740.0,
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        },
        {
            "id": 593027.0,
            "state": "CANCELED",
            "date": "2023-07-22T05:02:01Z",
            "amount": 30368.0,
            "currency_name": "Shilling",
            "currency_code": "TZS",
            "from": "Visa 1959232722494097",
            "to": "Visa 6804119550473710",
            "description": "Перевод с карты на карту",
        },
        {
            "id": 366176.0,
            "state": "EXECUTED",
            "date": "2020-08-02T09:35:18Z",
            "amount": 29482.0,
            "currency_name": "Rupiah",
            "currency_code": "IDR",
            "from": "Discover 0325955596714937",
            "to": "Visa 3820488829287420",
            "description": "Перевод с карты на карту",
        },
        {
            "id": 5380041.0,
            "state": "CANCELED",
            "date": "2021-02-01T11:54:58Z",
            "amount": 23789.0,
            "currency_name": "Peso",
            "currency_code": "UYU",
            "from": nan,
            "to": "Счет 23294994494356835683",
            "description": "Открытие вклада",
        },
    ]


def xlsx_arr() -> list[dict]:
    return [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
        {
            "id": 3598919.0,
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "amount": 29740.0,
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        },
        {
            "id": 593027.0,
            "state": "CANCELED",
            "date": "2023-07-22T05:02:01Z",
            "amount": 30368.0,
            "currency_name": "Shilling",
            "currency_code": "TZS",
            "from": "Visa 1959232722494097",
            "to": "Visa 6804119550473710",
            "description": "Перевод с карты на карту",
        },
        {
            "id": 366176.0,
            "state": "EXECUTED",
            "date": "2020-08-02T09:35:18Z",
            "amount": 29482.0,
            "currency_name": "Rupiah",
            "currency_code": "IDR",
            "from": "Discover 0325955596714937",
            "to": "Visa 3820488829287420",
            "description": "Перевод с карты на карту",
        },
        {
            "id": 5380041.0,
            "state": "CANCELED",
            "date": "2021-02-01T11:54:58Z",
            "amount": 23789.0,
            "currency_name": "Peso",
            "currency_code": "UYU",
            "from": nan,
            "to": "Счет 23294994494356835683",
            "description": "Открытие вклада",
        },
    ]
