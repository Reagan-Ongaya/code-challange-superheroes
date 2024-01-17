#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate
from flask_restful import Resource, 

from models import db, Hero

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

class Home(Resource):
  def get(self):
    return make_response({
        "massege": "welcome to api"
    })

class SuperHeroes(Resource):
  def get(self):
      heroes = Hero.

@app.route('/')
def home():
    return ''


if __name__ == '__main__':
    app.run(port=5555)
