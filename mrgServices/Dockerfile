# образ на основе которого создаём контейнер
FROM python:3.9.5-alpine

# рабочая директория внутри проекта
WORKDIR /app

# переменные окружения для python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install gunicorn

# устанавливаем зависимости
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# копируем содержимое текущей папки в контейнер
COPY . .
CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000
# CMD python manage.py makemigrations && python manage.py migrate && gunicorn main.wsgi:application --bind 0.0.0.0:8000