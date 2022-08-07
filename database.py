
from webbrowser import get
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from viewhandler.utilities.env import get_env


DATABASE_USER = get_env('DATABASE_USER')
DATABASE_PASSWORD = get_env('DATABASE_PASSWORD')
DATABASE_HOST = get_env('DATABASE_HOST')
DATABASE_PORT = get_env('DATABASE_PORT')
ENV=get_env('ENV')
DATABASE_NAME = get_env('DATABASE_NAME') if ENV == 'DEV' else get_env('TEST_DATABASE_NAME') 

DATABASE_URL= f'postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}'
db = SQLAlchemy()

def create_app():
    print('database url ---> ', DATABASE_URL)
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False    
    
    app.app_context().push()    
        
    with app.app_context():
        db.init_app(app)   
                     
    Migrate(app, db)
    from modles import customers, categories, buy_categories_materials, sell_categories_materials, customers_otp, admin, delivery, materials, matrials_categories, zone
    
    return app

def add(entity):
    db.session.add(entity)
    db.session.commit()
    