import pytest

from src.generators import card_number_generator
from tests.conftest import card_generator_tests


@pytest.mark.parametrize("start,stop,expected", card_generator_tests())
def test_card_number_generator(start, stop, expected) -> None:
    for idx, card_number in enumerate(card_number_generator(start, stop + 1)):
        assert card_number == expected[idx]