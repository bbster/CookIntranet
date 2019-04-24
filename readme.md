# CookIntranet
### HOW TO 배포

#### - 배포 사전준비
git 설치, docker 설치, docker-compose 설치

#### - 클라이언트 배포
1. ./scripts/update_client_build.sh
2. ./scripts/update_{DEPLOYMENT_LEVEL('local' or 'production')}_docker_server.sh

#### - 서버배포
1. git pull origin master
2. ./scripts/update_{DEPLOYMENT_LEVEL('local' or 'production')}_docker_server.sh

#### Nginx config reference
- https://www.linode.com/docs/web-servers/nginx/how-to-configure-nginx/
- https://www.nginx.com/resources/wiki/start/topics/examples/full/
- https://www.opentutorials.org/module/384/4526