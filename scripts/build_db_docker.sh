docker rm -f intranet_postgres
docker rmi -f $(docker images | grep "<none>" | awk "{print \$3}")
docker-compose -f docker-compose.yml up -d --build db