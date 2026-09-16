# BANKPROJECT
## Описание:
Bankproject - мой учебный проект, где я делаю виджет для банка

## Установка:
1. Клонируйте репозиторий
```
git clone https://github.com/LexaNovikov/bankproject.git
```

2. Установите poetry
```
pip install poetry
```

3. Установите зависимости
```
poetry install
```

## Использование:
Запустите test.py в директории tests

Для windows:
```
python tests/test.py
``` 

Для linux/macos
```
python3 tests/test.py
```
## Документация:
В пакете ```src``` лежат модули кода:

```masks.py```
Содержит функции маскировки карты и счета

```widget.py```
Содержит функцию распознавания карты и счета и в дальнейшем маскирует их

```processing.py``` 
Содержит функции фильтров по дате и статусу

В пакете ```tests``` содержатся модули и файлы для тестирования функций

```test.py ```
Модуль тестирования, тестит все функции

```get_date_tests.txt```
Тесты для функции get_date

```mask_account_card.txt```
Тесты для функции mask_account_card