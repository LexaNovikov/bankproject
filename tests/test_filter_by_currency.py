from src.generators import filter_by_currency
from tests.conftest import generators_list, rub_case, usd_case


def test_filter_by_currency_usd(test_list: list = generators_list(), expected: list = usd_case()) -> None:
    filtered = filter_by_currency(test_list, "USD")
    for i in range(2):
        assert next(filtered) == expected[i]


def test_filter_by_currency_rub(test_list: list = generators_list(), expected: list = rub_case()) -> None:
    filtered = filter_by_currency(test_list, "RUB")
    for i in range(2):
        assert next(filtered) == expected[i]
