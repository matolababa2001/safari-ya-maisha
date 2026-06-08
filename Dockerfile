FROM python:3.11

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN python manage.py migrate

RUN python manage.py collectstatic --noinput

CMD gunicorn safari_ya_maisha.wsgi:application --bind 0.0.0.0:10000