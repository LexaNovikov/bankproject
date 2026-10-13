import os.path
from unittest.mock import MagicMock, patch

import pytest

from src.read_sheets import read_xlsx
from tests.conftest import xlsx_arr


@patch("os.path.exists")
def test_read_xlsx_not_found(mock_exists: MagicMock) -> None:
    mock_exists.return_value = False
    with pytest.raises(FileNotFoundError) as e:
        read_xlsx("test.xlsx")
    assert str(e.value) == "Файл не найден"


@patch("os.path.isfile")
def test_read_xlsx_existing(mock_isfile: MagicMock) -> None:
    mock_isfile.return_value = False
    with pytest.raises(ValueError) as e:
        read_xlsx("/")
    assert str(e.value) == "Объект является директорией"


@patch("os.path.isfile")
@patch("os.path.exists")
def test_read_xlsx_not_empty(mock_exists: MagicMock, mock_isfile: MagicMock) -> None:
    mock_exists.return_value = True
    mock_isfile.return_value = True
    with pytest.raises(ValueError) as e:
        read_xlsx("test/test.json")
    assert str(e.value) == "Расширение файла не является xlsx"


@patch("pandas.read_excel")
@patch("os.path.isfile")
@patch("os.path.exists")
def test_read_xlsx(mock_exists: MagicMock, mock_isfile: MagicMock, mock_read_xlsx: MagicMock) -> None:
    mock_exists.return_value = True
    mock_isfile.return_value = True
    mock_read_xlsx.return_value.to_dict.return_value = xlsx_arr
    result = read_xlsx()
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base, "data", "transactions_excel.xlsx")
    mock_read_xlsx.assert_called_once_with(file_path)
    assert result == xlsx_arr
