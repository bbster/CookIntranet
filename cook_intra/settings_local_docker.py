from .settings_base import *
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'cookintranet',
        'USER': 'admin',
        'PASSWORD': 'dlwlehd12',
        'HOST': 'intranet_postgres',  # docker 컨테이너 이름
        'PORT': '5432',
    }
}
