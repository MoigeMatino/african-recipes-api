FROM python:3.10

# https://stackoverflow.com/questions/59812009/what-is-the-use-of-pythonunbuffered-in-docker-file
ENV PYTHONUNBUFFERED=1
ENV POETRY_VERSION=1.2.1

WORKDIR /api/app

RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="${PATH}:/root/.local/bin"
COPY pyproject.toml poetry.lock /api/
RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-interaction

COPY .env .

COPY ./app /api/app

CMD ["uvicorn", "routes:app", "--host", "0.0.0.0", "--port", "4002"]