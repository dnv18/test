import os
from decouple import config


class Config(object):
    basedir = os.path.abspath(os.path.dirname(__file__))

    # SECRET_KEY
    SECRET_KEY = config('SECRET_KEY', default='S#perS3crEt_007')

    # PSQL db
    SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}:{}/{}'.format(
        config('DB_ENGINE', default='postgresql'),
        config('DB_USERNAME', default='username'),
        config('DB_PASS', default='pass'),
        config('DB_HOST', default='localhost'),
        config('DB_PORT', default=5432),
        config('DB_NAME', default='db_name')
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
