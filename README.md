# Bank deposit

[![CI](https://github.com/Evkos-dev/bank_deposit/actions/workflows/bank_deposit_workflow.yml/badge.svg?branch=master)](https://github.com/Evkos-dev/bank_deposit/actions/workflows/bank_deposit_workflow.yml)

### Описание проекта
API сервис для расчета капитализации банковского вклада. Расчет происходит каждый месяц в число вклада.

### Пример запроса:
  ###### Пример POST запроса:
  `"/api/deposits/"`
```
  {
     "date": "01.01.2021",
     "periods": 3,
     "amount": 10000,
     "rate": 6
  }
```
  ###### Пример ответа:
```
  {
     "01.02.2021": 10050.0,
     "01.03.2021": 10100.25,
     "01.04.2021": 10150.75,
  }
```

### Стек технологий
- Python 3.11.1
- Django 4.1.6
- Django Rest Framework 3.14.0

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

`git clone https://github.com/Evkos-dev/bank_deposit.git`

`cd bank_deposit`

Запустить Docker:

`docker run --name bank_deposit -it -p 8000:8000 bank_deposit`

Запросы отправлять на адресс: 

`http://localhost:8000/api/deposits/`
