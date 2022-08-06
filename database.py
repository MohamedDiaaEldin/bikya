
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

DATABASE_URL='postgresql://mohamed:123@127.0.0.1:5432/recycling'
db = SQLAlchemy()

def create_app():
    print('database url ---> ', DATABASE_URL)
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False    
    
    # app_context().push()
    # db.init_app(app)    
    
    with app.app_context():
        db.init_app(app)   
         
    Migrate(app, db)
    from modles import customers, categories, buy_categories_materials, sell_categories_materials, customers_otp, admin, delivery, materials, matrials_categories, zone
    return app

def add(entity):
    db.session.add(entity)
    db.session.commit()
    