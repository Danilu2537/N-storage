# N-storage

Данный проект - реализация тестового задания.

### Описание
---
Первым этапом было проектирование базы данных по следующим параметрам. В компании N имеется несколько складов с техникой. На каждый склад закреплен сотрудник, отвечающий
за принятие и выдачу оборудования по поступающим накладным. У каждой единицы техники есть инвентарный номер,производитель, страна производства, стоимость и модель.

В первом приложении `storages` находятся модели `Storage`, `Employee`, `Technics`, отвечающие за хранение данных по складам, сотрудникам и технике соответственно.

Во втором приложении `movement` располагаются модели, отвечающие за логистику: `Units`, `Dispatch`, `Receipt`, отвечающие за количество техники на складах, выдаче техники и приеме соответственно.

![DB schema](https://github.com/Danilu2537/N-storage/blob/main/assets/db.png?raw=true)

Доступа к изменению через API количества товара нет, повлиять на это можно только через создание записи отпуска или приема товара. Про особенности работы с API можно узнать [здесь](#APIdoc)

Также был реализован фронтенд для просмотра [отчетов](#reports)

### Использовано
---
- Python 3.10
- Django 4.2
- Django REST Framework 3.14
- Plotly 5.17
- PostgreSQL 15.1
- Docker
- Docker-compose

### Установка
---
### Linux | WSL (Ubuntu)

1. Склонировать репозиторий

    ```bash
    git clone https://github.com/Danilu2537/N-storage
    ```
2. Установить `Docker` и `Docker-compose`

    ```bash
    sudo apt install docker docker-compose
    ```

3. Создать `.env` файл в корне проекта и заполнить согласно шаблону `.env.example`

    ```bash
    cd n-storage
    touch .env
    ```

### Миграции
---

1. Запустить базу данных для миграции

    ```bash
    sudo docker-compose up -d db
    ```

2. Применить миграции \
    Либо мигрировать, сгенерировать и импортировать тестовые записи

    > Для корректной работы скрипта необходима установка библиотек
    > Для установки `poetry` и нужных библиотек
    > ```bash
    > pip install poetry
    > poetry shell
    > poetry install
    > ```

    ```bash
    python ./scripts/create_and_load_data.py
    ```
    > Появится папка `fixtures` с копиями записей БД

    Либо применить только миграции

    > Они будут автоматически применены при запуске `docker-compose`

3. Создать суперпользователя для доступа в админку

    ```bash
    python manage.py createsuperuser
    ```
### Запуск
---
```bash
docker-compose up -d
```

Админка будет доступна по адресу: \
http://localhost/admin/

### <a id="reports"></a>Отчеты
Страницы отчетов доступны из корня приложения: \
    http://localhost/

![front-reports](https://github.com/Danilu2537/N-storage/blob/main/assets/report.png?raw=true)

### <a id="APIdoc"></a>Документация API
Документация доступна после запуска по адресам: \
    http://localhost/schema/ \
    http://localhost/schema/swagger-ui/ \
    http://localhost/schema/redoc/
