from unittest.mock import MagicMock, patch

from src.external_api import get_amount

url = "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=100.0"


@patch("requests.request")
def test_get_amount(mock_request: MagicMock) -> None:
    mock_request.return_value.json.return_value = {"result": "8482.389247"}
    assert get_amount({"amount": 100, "currency": {"code": "USD"}}) == 8482.389247
    mock_request.assert_called_once_with(
        "GET",
        url,
        headers={"apikey": "UatIZXc4xghqk8ZJmN9yEftD9JlBPhRV"},
        data={},
        params={"amount": "100.0", "from": "USD", "to": "RUB"},
    )


@patch("requests.request")
def test_get_amount_RUB(mock_request: MagicMock) -> None:
    mock_request.return_value.json.return_value = {"result": "100.0"}
    assert get_amount({"amount": 100, "currency": {"code": "RUB"}}) == 100.0
