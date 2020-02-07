FROM python:3

ENV PYTHONUNBUFFERED=1

RUN mkdir /var/rssbro
WORKDIR /var/rssbro

RUN pip install pip-tools
ADD requirements.in /var/rssbro/
RUN pip-compile requirements.in

RUN pip install --requirement requirements.txt

ADD rssbro /var/rssbro

CMD gunicorn rssbro.wsgi:application --bind 0.0.0.0:8000 --workers 1 --worker-class gevent
