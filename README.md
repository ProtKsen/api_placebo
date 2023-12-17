# API_Placebo

REST-api с базовым функционалом для управления структурой компании и правами сотрудников

* Приложение реализовано на **Django**, база данных - **PostgreSQL**, документация - **Swagger**, менеджер зависимостей - **poetry**.

### Использование

#### Установка

```bash
git clone git@github.com:ProtKsen/api_placebo.git
```

#### Установка poetry, выполняется один раз

```bash
pip install poetry
poetry config virtualenvs.in-project true
```

#### Установка зависимостей

```bash
poetry init
poetry install
```

#### Настройки окружения

Создать файл `.env` на базе `.env.default`. Для локальног запуска достаточно скопировать содержимое `.env.default`.


#### Установка docker, выполняется один раз

См. <https://docs.docker.com/engine/install/>

#### Запуск базы данных

```bash
docker-compose up -d db
```

#### Запуск приложения локально

```bash
cd api-placebo
python src/manage.py runserver
```

Документация доступна по адесу <http://127.0.0.1:8000/swagger-ui/>.
