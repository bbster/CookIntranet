FROM python:3.7.3
MAINTAINER LEE Ji Chan bbster12@gmail.com

# create server folder
WORKDIR /home/server/

# python packages
COPY ./requirements/requirements.txt/   /home/server/requirements/
RUN  pip install -r requirements/requirements.txt

# front-end source
COPY    ./_nuxt/                /home/server/_nuxt/
COPY    ./frontend/             /home/server/frontend/

# back-end source
COPY    ./manage.py             /home/server/
COPY    ./authen/               /home/server/authen/
COPY    ./cook_intra/           /home/server/cook_intra/
COPY    ./feeds/                /home/server/feeds/
