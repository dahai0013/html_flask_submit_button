FROM tiangolo/uwsgi-nginx-flask

ENV STATIC_INDEX 1

COPY ./app /app