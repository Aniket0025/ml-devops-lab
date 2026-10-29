FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --timeout=300 --retries=15 -r requirements.txt

COPY app.py hello.py test_hello.py ./

EXPOSE 5000

CMD ["python", "app.py"]