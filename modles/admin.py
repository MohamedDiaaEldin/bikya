
import sys
sys.path.append('..')
from sqlalchemy import  Column, String, Integer
from database import db

class Admin(db.Model):    
    ## fields
    id = Column(Integer, primary_key=True) 
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    def add(self):        
        db.session.add(self)
        db.session.commit()