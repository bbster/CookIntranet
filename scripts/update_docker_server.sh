#!/usr/bin/env bash
docker-compose -f docker-compose.yml up -d db
docker-compose -f docker-compose.yml up -d --build django

#docker-compose 파일 docker-compose.yml 상태 up -d 백그라운드 빌드 컨테이너이름
