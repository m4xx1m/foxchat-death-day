FROM python:3.10-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --no-cache-dir -r requirements.txt

COPY app app

CMD ["python", "-m", "app"]
