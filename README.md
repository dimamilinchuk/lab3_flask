# Лабораторна робота 3: Валідація, ORM та обробка помилок

## Опис проекту

Додаток для фінансового обліку з підтримкою:
- Обліку доходів та витрат
- Керування рахунками користувачів
- Автоматичного списання коштів при створенні витрат
- Валідації вхідних даних та обробки помилок
- Роботи з базою даних через ORM (SQLAlchemy)

Особливості реалізації (Варіант 0 - Облік доходів):
- Кожен користувач має персональний рахунок
- Кошти автоматично списуються з рахунку при додаванні витрат
- Перехід у негативний баланс заборонено (викликає помилку)
- Система підтримує множинні операції доходів/витрат

## Вимоги

- Python 3.10+
- Docker та Docker Compose
- Бібліотеки вказані у requirements.txt

## Швидкий старт

### 1. Клонування репозиторію
git clone <URL_вашого_репозиторію>
cd lab3_project


### 2. Налаштування оточення
Створіть .env файл у корені проекту:
POSTGRES_USER=admin
POSTGRES_PASSWORD=secret
POSTGRES_DB=finance_db
DATABASE_URL=postgresql://admin:secret@db:5432/finance_db


### 3. Запуск сервісів
docker-compose up -d db       # Запуск бази даних
docker-compose up app         # Запуск додатка


### 4. Виконання міграцій
flask db upgrade


## Структура проекту
├── app/
│   ├── __init__.py          # Фабрика додатку
│   ├── models.py            # ORM моделі
│   ├── schemas.py           # Marshmallow схеми
│   ├── routes/              # Блюпрінти API
│   │   ├── accounts.py
│   │   ├── transactions.py
│   │   └── ... 
├── migrations/              # Міграції бази даних
├── config.py                # Конфігурація додатку
├── docker-compose.yaml
└── requirements.txt


## API Ендпоінти

### Рахунки
- POST /accounts - Створення нового рахунку
- GET /accounts/{user_id} - Отримання балансу
- POST /accounts/{user_id}/deposit - Поповнення рахунку

### Транзакції
- POST /transactions/income - Додавання доходу
- POST /transactions/expense - Додавання витрати
- GET /transactions/{user_id} - Історія операцій

Приклад запиту:
curl -X POST http://localhost:5000/transactions/income \
  -H "Content-Type: application/json" \
  -d '{"user_id": 1, "amount": 1500, "description": "Зарплата"}'


## Валідація та обробка помилок
Додаток використовує:
- Валідацію даних через Marshmallow
- Глобальну обробку помилок
- HTTP статус коди для всіх відповідей

Приклад помилки:
{
  "error": "Insufficient funds",
  "message": "На рахунку недостатньо коштів для проведення операції"
}


## Залежності
Основні бібліотеки:
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Marshmallow
- psycopg2-binary

Встановлення:
pip install -r requirements.txt


## Локальна розробка
1. Запустіть тестувальний сервер:
FLASK_APP=app FLASK_ENV=development flask run


2. Для роботи з міграціями:
flask db init          # Ініціалізація (перший раз)
flask db migrate       # Створення нової міграції
flask db upgrade       # Застосування міграцій


## Тестування
Використовуйте Postman колекцію з прикладами запитів:
- Імпортуйте Finance API.postman_collection.json