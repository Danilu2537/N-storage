import json
import os
from random import randint

from faker import Faker

"""Количество складов (сотрудников генерируется такое же количество)"""
COUNT_STORAGES = 5

"""Количество единиц техники (диапазон общих остатков на складах 0-COUNT_TECHNICS)"""
COUNT_TECHNICS = 100


def load_storage() -> int:
    """Функция генерирует склады

    Returns:
        int: Последний id склада, для последующей привязки сотрудников
    """
    storages = [
        {
            'model': 'storages.storage',
            'fields': {'title': fake.company(), 'info': fake.text()},
        }  # Шаблон фикстуры для загрузки в БД
        for _ in range(COUNT_STORAGES)
    ]
    with open('fixtures/storages.json', 'w') as f:
        json.dump(storages, f, indent=4)  # Запись результатов в файл
    # Импорт данных в БД из файла при помощи django loaddata
    os.system('python manage.py loaddata fixtures/storages.json')
    # Сохранение импортированных значений из БД для последующего использования
    os.system(
        'python manage.py dumpdata storages.storage --indent 4 '
        '> fixtures/storages.json'
    )
    with open('fixtures/storages.json', 'r') as f:
        storages = json.load(f)
    # Возвращение последнего id для последующей привязки сотрудников
    # и количества на складах
    return max(map(lambda x: x['pk'], storages))


def load_employee(last_id_storage):
    """Функция генерирует сотрудников"""
    employees = [
        {
            'model': 'storages.employee',
            'fields': {'name': fake.name(), 'contacts': fake.email(), 'storage': i},
        }  # Шаблон сотрудника
        # Перебор последних id складов для привязки
        for i in range(last_id_storage, last_id_storage - COUNT_STORAGES, -1)
    ]
    with open('fixtures/employees.json', 'w') as f:
        json.dump(employees, f, indent=4)
    os.system('python manage.py loaddata fixtures/employees.json')
    os.system(
        'python manage.py dumpdata storages.employee --indent 4 '
        '> fixtures/employees.json'
    )  # Сохранение значений из БД


def load_technics() -> list[int]:
    """Функция генерации единиц техники

    Returns:
        list[int]: Список сгенерированных id единиц техники
    """
    technics = [
        {
            'model': 'storages.technic',
            'fields': {
                'id': fake.unique.pyint(),
                'model': fake.unique.license_plate(),
                'manufacturer': fake.company(),
                'country': fake.country(),
                'price': fake.pyint() * 100,
            },
        }  # Шаблон единицы техники
        # Генерация по количеству
        for _ in range(COUNT_TECHNICS)
    ]
    with open('fixtures/technics.json', 'w') as f:
        json.dump(technics, f, indent=4)
    os.system('python manage.py loaddata fixtures/technics.json')
    os.system(
        'python manage.py dumpdata storages.technic --indent 4 '
        '> fixtures/technics.json'
    )  # СОхранение значений из БД
    # Сохранение id для последующей привязки количества
    return list(map(lambda x: x['fields']['id'], technics))


def get_count_from_distribution(total, storages=COUNT_STORAGES) -> int:
    """Генератор для нормального распределения количества единиц техники,
    на основе количества складов


    Args:
        total (_type_): Всего единиц техники
        storages (_type_, optional): Количество складов. Defaults to COUNT_STORAGES.

    Yields:
        int: Возвращает по одному количество на склад
    """
    for i in range(storages, 0, -1):
        count = total // i
        total -= count
        yield count


def load_units(id_technics: list[int], last_id_storage: int):
    """Генерация количества единиц техники
    на склад

    Args:
        id_technics (_type_): id Единиц техники
        last_id_storage (_type_): Последний id склада
    """
    units = [
        {
            'model': 'movement.units',
            'fields': {'storage': storage, 'technic': technic, 'count': count},
        }  # Шаблон записи количества техники
        # Выбор по одной единице техники и одного ее общего количества
        for technic, total in zip(id_technics, range(COUNT_TECHNICS), strict=False)
        # Для каждой единицы техники перебор складов
        # и подсчет нужного количества для этого склада
        for storage, count in zip(
            sorted(
                range(last_id_storage, last_id_storage - COUNT_STORAGES, -1),
                key=lambda _: randint(0, 1),
            ),  # Перемешивание складов
            get_count_from_distribution(total),  # Генерация количества на склад
            strict=False,
        )
    ]
    with open('fixtures/units.json', 'w') as f:
        json.dump(units, f, indent=4)
    os.system('python manage.py loaddata fixtures/units.json')
    os.system(
        'python manage.py dumpdata movement.units --indent 4 > fixtures/units.json'
    )  # Сохранение значений из БД


fake = Faker(locale='ru_RU')  # Инициализация фейкового генератора
if not os.path.exists('fixtures'):
    os.system('mkdir fixtures')  # Создание папки fixtures

os.system('python manage.py migrate')  # Миграция БД

# Вызов всех функция для генерации и импорта
last_id_storage = load_storage()
load_employee(last_id_storage)
ids_technics = load_technics()

load_units(ids_technics, last_id_storage)
