import pytest

from src.widget import get_date


@pytest.mark.parametrize(
    "data, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2026-09-19T02:32:19.244334", "19.09.2026"),
        ("1991-08-23T01:34:32.123232", "23.08.1991"),
    ],
)
def test_get_date(data: str, expected: str) -> None:
    assert get_date(data) == expected
    return
