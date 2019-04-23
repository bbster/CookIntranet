#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
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
    # 장고 프로그램은 시작될 때 세팅파일을 불러오도록 되어있음.
    # 이 세팅파일을 불러올 때, OS 환경변수 "DJANGO_SETTINGS_MODULE" 의 값을 보고 가져오게 되어있다.
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
