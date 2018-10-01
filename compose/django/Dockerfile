FROM python:latest
ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND noninteractive
ENV TERM xterm

# update, upgrade, and install packages
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y apt-utils \
    && apt-get install -y curl git less man nano sudo wget

# configure apt-utils (fixes warnings)
RUN dpkg-reconfigure apt-utils

# set some useful defaults
RUN echo "alias ls='ls --color'" >> /etc/bash.bashrc
RUN echo "alias grep='grep --color=auto'" >> /etc/bash.bashrc

# upgrade pip
RUN pip install --upgrade pip

# install requirements
COPY ./requirements /requirements
RUN pip install -r /requirements/dev.txt

# copy start script and make executable
COPY ./compose/django/start /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start

# install editable package
COPY . /djcorecap
RUN pip install -e /djcorecap

# create and configure django app for djcorecap development
RUN django-admin startproject app
RUN echo "ALLOWED_HOSTS = ['*']" >> /app/app/settings.py
RUN echo "INSTALLED_APPS += ['djcorecap']" >> /app/app/settings.py
RUN echo "INSTALLED_APPS += ['crispy_forms']" >> /app/app/settings.py
RUN echo "from django.conf.urls import include, url" >> /app/app/urls.py
RUN echo "urlpatterns += [url(r'^djcorecap/', include('djcorecap.urls'))]" \
    >> /app/app/urls.py

WORKDIR /app
