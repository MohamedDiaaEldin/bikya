import sys
sys.path.append('..')
from sqlalchemy import  Column, String, Integer, Float, Boolean, ForeignKey
from database import db

class SellCategorymatrial(db.Model):    
    id = Column(Integer, primary_key=True)
    matrial_id = Column(Integer, ForeignKey('matrial.id'))
    category_id = Column(Integer, ForeignKey('category.id'))
    delivery_id = Column(Integer, ForeignKey('delivery.id'))
    customer_id = Column(Integer, ForeignKey('customer.id')) 
    date = Column(String, nullable=False) 
    time = Column(String, nullable=False) 
    weight = Column(Float, nullable=False)
    points =  Column(Float, nullable=False)  # default false 
    done =  Column(Boolean, nullable=False)
    def add(self):        
        db.session.add(self)
        db.session.commit()