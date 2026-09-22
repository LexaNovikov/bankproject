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
 
3. Инициализируйте poetry
```
poetry init
```

4. Установите зависимости
```
poetry install
```

## Использование:
Запустите pytest в директории tests

```
pytest ./tests
``` 

## Документация:
В пакете ```src``` лежат модули кода:

```masks.py```
Содержит функции маскировки карты и счета

```widget.py```
Содержит функцию распознавания карты и счета и в дальнейшем маскирует их

```processing.py``` 
Содержит функции фильтров по дате и статусу

```generators.py```
Содержит функции генерации номера карты, фильтрации транзакций по валютам и вывод информации по транзакции 

В пакете ```tests``` содержатся модули и файлы для тестирования функций

```conftest.py```
Модуль, содержащий фикстуры pytest

```test_mask_account_card.py```
Модуль тестирования, предназначенный для тестирования функции ```mask_account_card.py``` из модуля ```widget.py```

```test_get_date.py```
Модуль тестирования, предназначенный для тестирования функции ```get_date.py``` из модуля ```widget.py```

```test_filter_by_state.py```
Модуль тестирования, предназначенный для тестирования функции ```filter_by_state.py``` из модуля ```processing.py```

```test_sort_by_date.py```
Модуль тестирования, предназначенный для тестирования функции ```sort_by_date.py``` из модуля ```processing.py```

```test_card_number_generator```
Модуль тестирования, предназначенный для тестирования функции ```card_number_generator``` из модуля ```generators.py```

```test_filter_by_currency```
Модуль тестирования, предназначенный для тестирования функции ```filter_by_currency``` из модуля ```generators.py```

```test_transaction_descriptions```
Модуль тестирования, предназначенный для тестирования функции ```transaction_descriptions``` из модуля ```generators.py```