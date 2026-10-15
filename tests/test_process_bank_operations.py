from src.filters import process_bank_operations


def test_process_bank_operations() -> None:
    assert process_bank_operations(
        [
            {"id": 1, "description": "test"},
            {"id": 2, "description": "cats"},
            {"id": 3, "description": "dogs"},
            {"id": 4, "description": "cats"},
        ],
        ["test", "cats"],
    ) == {"test": 1, "cats": 2}


def test_process_bank_operations_without_result() -> None:
    assert (
        process_bank_operations(
            [
                {"id": 1, "description": "test"},
                {"id": 2, "description": "cats"},
                {"id": 3, "description": "dogs"},
                {"id": 4, "description": "cats"},
            ],
            ["faketext"],
        )
        == {}
    )


def test_process_bank_operations_without_description() -> None:
    assert process_bank_operations(
        [
            {"id": 1, "description": "test"},
            {"id": 2},
            {"id": 3, "description": "dogs"},
            {"id": 4, "description": "cats"},
        ],
        ["cats", "dogs"],
    ) == {"cats": 1, "dogs": 1}
