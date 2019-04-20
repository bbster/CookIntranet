#!/usr/bin/env bash
# docker-compose 파일 docker-compose.yml 상태 up -d 백그라운드 빌드 컨테이너이름
docker-compose -f docker/docker-compose.yml up -d --build django

