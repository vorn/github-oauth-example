FROM python:3.9-slim

ARG APP_USER=appuser
RUN groupadd -r ${APP_USER} && useradd --no-log-init -r -g ${APP_USER} ${APP_USER}

COPY requirements.txt /app/
COPY src/ /app/

WORKDIR /app

# Needed to build uwsgi
RUN apt-get update
RUN apt-get install -y --no-install-recommends build-essential libpcre3-dev libpq-dev mime-support libpcre3

RUN pip install -r requirements.txt
RUN pip install uwsgi

EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=github_oauth.settings

RUN chown -R ${APP_USER}:${APP_USER} /app

USER ${APP_USER}:${APP_USER}

RUN python manage.py migrate --no-input
RUN python manage.py setup_github_app

RUN mkdir /app/static
RUN DATABASE_URL='' python manage.py collectstatic --noinput

# Basic uWSGI settings, also serving static files
ENV UWSGI_WSGI_FILE=/app/github_oauth/wsgi.py
ENV UWSGI_HTTP_SOCKET=:8000 UWSGI_MASTER=1 UWSGI_HTTP_AUTO_CHUNKED=1 UWSGI_HTTP_KEEPALIVE=1 UWSGI_LAZY_APPS=1 UWSGI_WSGI_ENV_BEHAVIOR=holy
ENV UWSGI_WORKERS=2 UWSGI_THREADS=4
ENV UWSGI_STATIC_MAP="/static/=/app/static/" UWSGI_STATIC_EXPIRES_URI="/static/.*\.[a-f0-9]{12,}\.(css|js|png|jpg|jpeg|gif|ico|woff|ttf|otf|svg|scss|map|txt) 315360000"

CMD ["uwsgi", "--show-config", "--master"]
