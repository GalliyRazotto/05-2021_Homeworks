# Чтобы запустить приложение используйте команду  docker run -p 8000:8000 web-app

FROM python:3.9.6-buster

WORKDIR /app

RUN pip install poetry

RUN poetry config virtualenvs.create false

COPY pyproject.toml .
COPY poetry.lock .

RUN poetry install

COPY homework_03 .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host=0.0.0.0"]