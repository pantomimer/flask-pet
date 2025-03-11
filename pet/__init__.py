from flask import Flask

from lib.db import init_db

app = Flask(__name__) # appがflask本体に

app.config.from_object('pet.config')

app.config.from_object('lib.config')

init_db(app)
import pet.views