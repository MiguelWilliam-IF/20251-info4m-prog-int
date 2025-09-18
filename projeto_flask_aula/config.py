import secrets
import urllib.parse as parse

class Config:
    SECRET_KEY = secrets.token_hex(16)
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:{}@127.0.0.1:3306/projeto_flask_aula".format(parse.quote("labinfo"))