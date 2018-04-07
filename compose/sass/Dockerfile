FROM debian:latest
ENV DEBIAN_FRONTEND noninteractive
ENV TERM xterm

# update, upgrade, and install packages
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y apt-utils \
    && apt-get install -y nano less make \
    && apt-get install -y build-essential \
    && apt-get install -y ruby ruby-dev

# configure apt-utils (fixes warnings)
RUN dpkg-reconfigure apt-utils

# set some useful defaults
RUN echo "alias ls='ls --color'" >> /etc/bash.bashrc
RUN echo "alias grep='grep --color=auto'" >> /etc/bash.bashrc

# install sass
RUN gem install sass --no-user-install

WORKDIR /static
