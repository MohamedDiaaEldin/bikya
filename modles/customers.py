import sys
sys.path.append('..')

from sqlalchemy import  Column, String, Integer, Float
from database import db, add
# from flask import current_app.db as db
# from 
from flask.cli import with_appcontext



class Customer(db.Model):
    __tablename__ = 'customer'  
    id = Column(Integer, primary_key=True) 
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)    
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)    
    address = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    points = Column(Float, nullable=False)
    
    
    def add(self):        
        db.session.add(self)
        db.session.commit()


