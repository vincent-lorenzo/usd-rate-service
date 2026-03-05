FROM python:3.11-slim

WORKDIR /app

COPY services/web/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY services/web .

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]