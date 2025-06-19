import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'all-you-need-is-love')
    DB_HOST = os.getenv('DB_HOST')
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')