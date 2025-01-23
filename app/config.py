import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:root@localhost/postgres')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
