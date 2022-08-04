import sys

sys.path.append('..')

from sqlalchemy import  Column, Integer, String
# from sqlalchemy.orm import relationship
from database import db

print('categories called')
class Category(db.Model):    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)        
    def add(self):        
        db.session.add(self)
        db.session.commit()
