# Hotel Booking API

## О проекте

Этот проект представляет собой API для системы бронирования отелей, разработанный с использованием FastAPI.

## Требования

- Python 3.x
- FastAPI
- SQLAlchemy
- ...

## Установка

1. Клонировать репозиторий:

    ```bash
    git clone https://github.com/yourusername/hotel-booking-api.git
    cd hotel-booking-api
    ```

2. Создать виртуальное окружение и установить зависимости:

    ```bash
    python -m venv venv
    source venv/bin/activate  # для Unix/Mac
    .\venv\Scripts\activate  # для Windows
    pip install -r requirements.txt
    ```

3. Переименовать файл .env_example --> .env и заполнить его.

3. Настроить базу данных и конфигурацию в файле `config.py`.

4. Запустить приложение:

    ```bash
    uvicorn main:app --reload
    ```

5. Перейти по адресу [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) для доступа к документации API.

## Функциональности

- Регистрация и аутентификация пользователей.
- Получение списка отелей и комнат.
- Бронирование номеров.
- ...

Пример запроса на регистрацию пользователя:

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/auth/register/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "email": "user@example.com",
  "password": "securepassword"
}'
