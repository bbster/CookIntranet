"""
WSGI config for cook_intra project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

DEPLOYMENT_LEVEL = os.environ.setdefault('DEPLOYMENT_LEVEL', "development")
# => 해석순서
# 1. 환경변수들 중 DEPLOYMENT_LEVEL 를 가져온다.  =>
# 2. 1번에서 잘 가져와졌다면? 그걸 반환한다..
# 3. 1번에서 안가져와졌으면? 뒤에값을 환경변수 DEPLOYMENT_LEVEL 에 넣고 그 값을 반환한다.

if DEPLOYMENT_LEVEL == "development":
    setting_file_name = "settings_development"
elif DEPLOYMENT_LEVEL == "local":
    setting_file_name = "settings_local_docker"
elif DEPLOYMENT_LEVEL == "production":
    setting_file_name = "settings_production_docker"

os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'cook_intra.{setting_file_name}')

application = get_wsgi_application()
