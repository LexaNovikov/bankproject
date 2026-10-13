import os.path
from unittest.mock import MagicMock, patch

import pytest

from src.read_sheets import read_csv
from tests.conftest import csv_arr


@patch("os.path.exists")
def test_read_csv_not_found(mock_exists: MagicMock) -> None:
    mock_exists.return_value = False
    with pytest.raises(FileNotFoundError) as e:
        read_csv("test.csv")
    assert str(e.value) == "Файл не найден"


@patch("os.path.isfile")
def test_read_csv_existing(mock_isfile: MagicMock) -> None:
    mock_isfile.return_value = False
    with pytest.raises(ValueError) as e:
        read_csv("/")
    assert str(e.value) == "Объект является директорией"


@patch("os.path.isfile")
@patch("os.path.exists")
def test_read_csv_not_empty(mock_exists: MagicMock, mock_isfile: MagicMock) -> None:
    mock_exists.return_value = True
    mock_isfile.return_value = True
    with pytest.raises(ValueError) as e:
        read_csv("test/test.json")
    assert str(e.value) == "Расширение файла не является csv"


@patch("pandas.read_csv")
@patch("os.path.isfile")
@patch("os.path.exists")
def test_read_csv(mock_exists: MagicMock, mock_isfile: MagicMock, mock_read_csv: MagicMock) -> None:
    mock_exists.return_value = True
    mock_isfile.return_value = True
    mock_read_csv.return_value.to_dict.return_value = csv_arr
    result = read_csv()
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base, "data", "transactions.csv")
    mock_read_csv.assert_called_once_with(file_path, delimiter=";")
    assert result == csv_arr
