import sys
sys.path.append('..')
from sqlalchemy import  Column, String, Integer, ForeignKey
from database import db

class Delivery(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)    
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    zone_id = Column(Integer, ForeignKey('zone.id'))

    def add(self):        
        db.session.add(self)
        db.session.commit()