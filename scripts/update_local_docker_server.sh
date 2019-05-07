#!/usr/bin/env bash
# 내 노트북에서 로컬환경 도커를 만들땐 이 스크립트를 사용함
docker rmi -f $(docker images | grep "<none>" | awk "{print \$3}")
docker-compose -f docker-compose.yml up -d db
docker-compose -f docker-compose.yml -f docker-compose/docker-compose-local.yml up -d --build django

#docker-compose 파일 docker-compose.yml 상태 up -d 백그라운드 빌드 컨테이너이름
