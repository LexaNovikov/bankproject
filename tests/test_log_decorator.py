import pytest

from src.decorators import log


def test_log_no_error_in_console(capsys: pytest.CaptureFixture[str]) -> None:
    """Функция, тестирующая декоратор log с выводом результата в консоль без ошибок"""

    @log()
    def add(x: int, y: int) -> int:
        return x + y

    add(2, 1)
    captured = capsys.readouterr()
    assert captured.out == "add, ok\n"


def test_log_with_error_in_console(capsys: pytest.CaptureFixture[str]) -> None:
    """Функция, тестирующая декоратор log с выводом результата в консоль с ошибкой неверного типа данных"""

    @log()
    def add(x: int, y: int) -> int:
        return x + y

    add("3", 1)
    captured = capsys.readouterr()
    assert captured.out.strip() == "add error: can only concatenate str (not \"int\") to str. Inputs: ('3', 1), {}"


def test_log_no_error_in_file() -> None:
    """Функция, тестирующая декоратор log с выводом результата в файл без ошибок"""

    @log("./src/log")
    def add(x: int, y: int) -> int:
        return x + y

    add(2, 1)
    with open("./src/log") as file:
        assert file.readlines()[-2].strip() == "add, ok"


def test_log_error_in_file() -> None:
    """Функция, тестирующая декоратор log с выводом результата в файл с ошибкой неверного типа данных"""

    @log("./src/log")
    def add(x: int, y: int) -> int:
        return x + y

    add("3", 1)
    with open("./src/log") as file:
        assert (
            file.readlines()[-2].strip()
            == "add error: can only concatenate str (not \"int\") to str. Inputs: ('3', 1), {}"
        )
