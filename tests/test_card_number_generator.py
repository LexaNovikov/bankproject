import pytest

from src.generators import card_number_generator
from tests.conftest import card_generator_tests


@pytest.mark.parametrize("start,stop,expected", card_generator_tests())
def test_card_number_generator(start: int, stop: int, expected: tuple[str]) -> None:
    for idx, card_number in enumerate(card_number_generator(start, stop)):
        assert card_number == expected[idx]


def test_card_number_generator_value_error() -> None:
    with pytest.raises(ValueError) as e:
        for card_number in card_number_generator(56, 3):
            print(card_number)
    assert str(e.value) == "Начало диапазона не должно быть больше конца диапазона"


def test_card_number_generator_error() -> None:
    with pytest.raises(ValueError) as e:
        for card_number in card_number_generator(-1, 1000000000000000000000):
            print(card_number)
    assert str(e.value) == "Начало диапазона должно быть строго больше 0, а конец диапазона меньше 9999999999999999"
