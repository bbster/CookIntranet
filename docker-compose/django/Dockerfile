#Use python 3
FROM python:3.7.3
MAINTAINER LEE Ji Chan bbster12@gmail.com

#create server folder
WORKDIR /home/server/

#Python Packages
COPY ./requirements/requirements.txt/   /home/server/requirements/
RUN  pip install -r requirements/requirements.txt

#Project source
COPY    ./manage.py            /home/server/
COPY    ./.vscode/             /home/server/.vscode/
COPY    ./_nuxt/                /home/server/_nuxt/
COPY    ./authen/               /home/server/authen/
COPY    ./cook_intra/           /home/server/cook_intra/
COPY    ./feeds/                /home/server/feeds/
COPY    ./frontend/             /home/server/frontend/

