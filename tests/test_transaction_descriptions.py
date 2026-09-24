from src.generators import transaction_descriptions
from tests.conftest import generators_list, transactions_descriptions


def test_transaction_descriptions(
    generator_list: list[dict] = generators_list(), expected: list[str] = transactions_descriptions()
) -> None:
    descriptions = transaction_descriptions(generator_list)
    for i in range(4):
        assert next(descriptions) == expected[i]
