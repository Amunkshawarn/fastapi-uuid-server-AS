
FROM python:3.11

WORKDIR /app

COPY app/pyproject.toml app/poetry.lock ./  
COPY app ./app

RUN curl -sSL https://install.python-poetry.org | python3 -  && \
    export PATH="/root/.local/bin:$PATH"

RUN /root/.local/bin/poetry install --no-root  # Use absolute path

EXPOSE 8000

CMD ["/root/.local/bin/poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
