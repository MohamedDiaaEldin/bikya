import sys
sys.path.append('..')
from sqlalchemy import  Column, String, Integer, Float, ForeignKey, Boolean
from database import db

class BuyCategoryMatrial(db.Model):
    id = Column(Integer, primary_key=True)
    matrial_id = Column(Integer,  ForeignKey('matrial.id'))
    category_id = Column(Integer, ForeignKey('category.id'))        
    customer_id = Column(Integer, ForeignKey('customer.id'))            
    date = Column(String, nullable=False) 
    time = Column(String, nullable=False) 
    weight = Column(Float, nullable=False)
    price =  Column(Float, nullable=False)
    done =  Column(Boolean, nullable=False)
 