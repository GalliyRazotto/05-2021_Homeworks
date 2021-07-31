# Чтобы запустить приложение используйте команду  docker run -p 8080:8000 web-app
FROM python:3.9.6-buster

WORKDIR /app

RUN pip install poetry

RUN poetry config virtualenvs.create false

COPY homework_03 .
COPY pyproject.toml .
COPY poetry.lock .

RUN poetry install

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host=0.0.0.0"]