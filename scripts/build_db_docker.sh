docker rm -f django_postgres
docker-compose -f docker-compose.yml up -d --build db