import json
from unittest.mock import patch

import pytest

from src.utils import get_operations_data
from tests.conftest import mock_arr


@patch("builtins.open")
def test_get_operations_data(mock_open):
    mock_file = mock_open.return_value.__enter__.return_value
    mock_file.read.return_value = json.dumps(mock_arr())
    assert get_operations_data() == mock_arr()
    mock_open.assert_called_once()


@patch("builtins.open")
def test_get_operations_data_error(mock_open):
    mock_file = mock_open.return_value.__enter__.return_value
    mock_file.read.return_value = mock_arr()
    assert get_operations_data() == []
    mock_open.assert_called_once()
