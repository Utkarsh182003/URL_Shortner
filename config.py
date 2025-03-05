import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'mysecretrandomkey2023'  # Change this to a secure random key
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'urls.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
