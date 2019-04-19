FROM python:3.7.3
MAINTAINER bbster12@gmail.com

# Home
WORKDIR /home/service/

# Python packages
COPY    ./requirements/requirements.txt/     /home/service/requirements/
# COPY   ./requirements/development.txt/    /home/service/requirements/
RUN pip install -r requirements/requirements.txt

# Project sources
COPY    ./manage.py         /home/service/
COPY    ./authen/           /home/service/authen/
COPY    ./feeds/            /home/service/feeds/
COPY    ./cook_intra/       /home/service/cook_intra/
COPY    ./frontend/         /home/service/frontend/
COPY    ./runserver.sh     /home/service/

# PORT
EXPOSE 8000

# ENTRYPOINT
ENTRYPOINT ["./runserver.sh"]




## Nginx install
#wkrRUN     apt-get -y install nginx


###########################################################################################
#
## zsh
#RUN     apt-get install -y zsh
#RUN     wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh || true
#RUN     chsh -s /usr/bin/zsh
#RUN     apt-get -y update


###pyenv install
#RUN     apt-get -y update
#RUN     apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm
#RUN     curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
#RUN     cd ~
#RUN     echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc
#RUN     echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
#RUN     echo 'eval "$(pyenv init -)"' >> ~/.bashrc
#
#RUN     /bin/bash
#ENV     PATH /root/.pyenv/bin:$PATH
#RUN     pyenv install 3.7.3
#RUN     pyenv virtualenv 3.7.3 myenv
#


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
#RUN         pyenv install 3.7.3
#
## pyenv settings
#RUN         echo 'export PATH="/root/.pyenv/bin:$PATH"' >> ~/.zshrc
#RUN         echo 'eval "$(pyenv init -)"' >> ~/.zshrc
#RUN         echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc
#
## pyenv virtualenv
#RUN         pyenv virtualenv 3.7.3 app
##
### uWGSI install
##RUN         /root/.pyenv/versions/app/bin/pip install uwsgi
##
#
##
### supervisord install
##RUN         apt-get -y install supervisor
##
### here