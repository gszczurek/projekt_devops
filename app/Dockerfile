# BUILDER
FROM python:3.12-slim AS builder

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY src/ ./src/
COPY alembic.ini /app/
COPY migrations/ /app/migrations/

# TEST
FROM builder AS test

ENV PYTHONPATH=/app/src

RUN pip install pytest pytest-flask

RUN pytest src/tests/ --maxfail=1 --disable-warnings -v

# FINAL
FROM python:3.12-slim AS final

WORKDIR /app

COPY --from=builder /usr/local /usr/local
COPY --from=builder /app/src/ ./src/
COPY --from=builder /app/migrations/ ./migrations/
COPY --from=builder /app/alembic.ini ./alembic.ini

ENV PYTHONPATH=/app/src
ENV FLASK_APP=app
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000

CMD ["flask", "run"]
