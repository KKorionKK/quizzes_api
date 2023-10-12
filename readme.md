# Как это завести?

## Настройка переменных окружения

Требуемые переменные окружения перечислены ниже:
```
DB_NAME = "quiz_database"
PG_USER = "root"
PG_PASSWORD = "123"
DB_ADAPTER = "postgresql+asyncpg"
DB_HOST = "database"
DB_PORT = "5432"
```
**Не забывайте, что переменные `DB_NAME, PG_USER, PG_PASSWORD и DB_PORT` должны совпадать с переменными в файле docker-compose сервиса database. А `DB_HOST` должен быть названием сервиса в docker-compose файле**

## Запуск
1. Перейдите в директорию проекта
2. Настройте переменные окружения в **.env** файле в **корневом** каталоге проекта
3. Введите в терминале команду `docker-compose up`
4. Перейдите по адресу [localhost:8000/docs](localhost:8000/docs) для проверки работы

## Тестовый запрос
Тестовый запрос, выполненный через CURL
```commandline
curl -X 'POST' \
  'http://localhost:8000/v1/quiz/get_quiz' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "questions_num": 1
}'
```
---
## О сервере
Взаимодействие происходит с СУБД **PostgreSQL** через асинхронную сессию **SQLAlchemy**.
Сервер поднят на **FastAPI**, валидация данных идет через **Pydantic**.
Тесты написаны на **Pytest**. А инициализация БД происходит через **Alembic**.