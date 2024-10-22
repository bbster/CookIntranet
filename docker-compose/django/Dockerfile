# Use python 3
FROM python:3.7.3
MAINTAINER LEE Ji Chan bbster12@gmail.com

# create server folder
WORKDIR /home/server/
RUN mkdir /home/server/media/

# service for web server
RUN apt-get update
RUN apt-get install -y build-essential nginx supervisor postgresql-client g++ automake1.11 perl libffi-dev vim

# Python Packages
RUN pip install --upgrade pip
COPY ./requirements/base.txt/   /home/server/requirements/
RUN  pip install -r requirements/base.txt

# server source

COPY    ./manage.py                 /home/server/
COPY    ./.vscode/                  /home/server/.vscode/
COPY    ./_nuxt/                    /home/server/_nuxt/
COPY    ./authen/                   /home/server/authen/
COPY    ./base/                     /home/server/base/
COPY    ./cook_intra/               /home/server/cook_intra/
COPY    ./feeds/                    /home/server/feeds/
COPY    ./scheduler/                /home/server/scheduler/
COPY    ./media/                    /home/server/media/


# client source
COPY    ./client_build/             /home/server/client/

# service run scripts
COPY    ./docker_entrypoint.sh    /home/server/
RUN     echo "daemon off;" >> /etc/nginx/nginx.conf
RUN     rm /etc/nginx/sites-enabled/default
COPY    ./docker-compose/nginx.conf          /etc/nginx/sites-enabled/cook_server_nginx.conf
COPY    ./docker-compose/supervisord.conf    /etc/supervisor/conf.d/cook_server_supervisord.conf
COPY    ./docker-compose/uwsgi.ini           /home/server/uwsgi.ini

EXPOSE 80

ENTRYPOINT ["./docker_entrypoint.sh"]
