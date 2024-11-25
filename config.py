import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///instance/chocolate.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'dev'