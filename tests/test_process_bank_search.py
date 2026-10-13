from src.filters import process_bank_search


def test_process_bank_search() -> None:
    assert process_bank_search(
        [
            {"id": 1, "description": "test"},
            {"id": 2, "description": "cats"},
            {"id": 3, "description": "dogs"},
            {"id": 4, "description": "cats"},
        ],
        "test",
    ) == [{"id": 1, "description": "test"}]


def test_process_bank_search_without_result() -> None:
    assert (
        process_bank_search(
            [
                {"id": 1, "description": "test"},
                {"id": 2, "description": "cats"},
                {"id": 3, "description": "dogs"},
                {"id": 4, "description": "cats"},
            ],
            "faketext",
        )
        == []
    )


def test_process_bank_search_without_description() -> None:
    assert process_bank_search(
        [
            {"id": 1, "description": "test"},
            {"id": 2},
            {"id": 3, "description": "dogs"},
            {"id": 4, "description": "cats"},
        ],
        "cats",
    ) == [{"id": 4, "description": "cats"}]
