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
RUN pip install -r /requirements/test.txt

# install editable package
COPY . /djcorecap
RUN pip install -e /djcorecap

WORKDIR /djcorecap
