FROM python:3.11.1-slim

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt --no-cache-dir

COPY . .

CMD ["python", "bank_deposit/manage.py", "runserver", "0:8000"]