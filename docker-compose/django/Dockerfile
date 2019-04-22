
#Use python 3
FROM python:3.7.3
MAINTAINER LEE Ji Chan bbster12@gmail.com

#create server folder
WORKDIR /home/server/

#Python Packages
COPY ./requirements/base.txt/   /home/server/requirements/
RUN  pip install -r requirements/base.txt

#Project source
COPY    ./manage.py            /home/server/
COPY    ./.vscode/             /home/server/.vscode/
COPY    ./_nuxt/                /home/server/_nuxt/
COPY    ./authen/               /home/server/authen/
COPY    ./cook_intra/           /home/server/cook_intra/
COPY    ./feeds/                /home/server/feeds/
COPY    ./frontend/             /home/server/frontend/


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