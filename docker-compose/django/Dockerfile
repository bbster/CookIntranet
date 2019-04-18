#Dockerfile.base


FROM ubuntu:16.04
RUN echo "helo"
MAINTAINER bbster12@naver.com
WORKDIR /home/service/

COPY ./manage.py         /home/service/
COPY ./authen/          /home/service/authen/
COPY ./feeds/          /home/service/feeds/
COPY ./TEST/          /home/service/TEST/
COPY ./docker-init.sh          /home/service/docker-init.sh

RUN /home/service/docker-init.sh
# RUN apt-get -y update

#RUN         apt-get -y update
#RUN         apt-get -y dist-upgrade
#RUN         apt-get install -y python-pip git vim
#RUN         ln -snf /usr/share/zoneinfo/Asia/Seoul /etc/localtime && \
#            echo "Asia/Seoul" > /etc/timezone
#
## pyenv
#RUN         apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
#libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
#xz-utils tk-dev
#RUN         curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
#ENV         PATH /root/.pyenv/bin:$PATH
#RUN         pyenv install 3.6.3
#
## zsh
#RUN         apt-get install -y zsh
#RUN         wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh || true
#RUN         chsh -s /usr/bin/zsh
#
## pyenv settings
#RUN         echo 'export PATH="/root/.pyenv/bin:$PATH"' >> ~/.zshrc
#RUN         echo 'eval "$(pyenv init -)"' >> ~/.zshrc
#RUN         echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc
#
## pyenv virtualenv
#RUN         pyenv virtualenv 3.6.3 app
#
## uWGSI install
#RUN         /root/.pyenv/versions/app/bin/pip install uwsgi
#
## Nginx install
#RUN         apt-get -y install nginx
#
## supervisord install
#RUN         apt-get -y install supervisor
#
## here