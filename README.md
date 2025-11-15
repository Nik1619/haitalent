# Haitalent QnA Project

Проект представляет собой веб-приложение на Django с базой данных PostgreSQL, предназначенное для работы с вопросами и ответами (QnA).
Все компоненты запускаются в контейнерах Docker.


```
### Модели
- **Question** – вопрос
  - `id`: int
  - `text`: str (текст вопроса)
  - `created_at`: datetime

- **Answer** – ответ на вопрос
  - `id`: int
  - `question_id`: int (ссылка на Question)
  - `user_id`: str (идентификатор пользователя)
  - `text`: str (текст ответа)
  - `created_at`: datetime
#### Вопросы (Questions)
- `GET /api/questions/` — список всех вопросов
- `POST /api/questions/` — создать новый вопрос
- `GET /api/questions/{id}/` — получить вопрос и все ответы на него
- `DELETE /api/questions/{id}/` — удалить вопрос (вместе с ответами)

#### Ответы (Answers)
- `POST /api/questions/{id}/answers/` — добавить ответ к вопросу
- `GET /api/answers/{id}/` — получить конкретный ответ
- `DELETE /api/answers/{id}/` — удалить ответ
```

**Запуск проекта через Docker Compose**

Клонируйте репозиторий

```bash
git clone <URL_репозитория>
cd haitalent
```

Постройте Docker-образы

```bash
docker compose build --no-cache
```

Запустите контейнеры

```bash
docker compose up
```

Создание миграций для изменений в моделях:

```bash
docker compose run --rm web python manage.py makemigrations
```

Применение миграций к базе данных:

```bash
docker compose run --rm web python manage.py migrate
```

Остановка проекта

```bash
docker compose down
```
