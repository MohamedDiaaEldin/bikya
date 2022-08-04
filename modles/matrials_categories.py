import sys
sys.path.append('..')
from sqlalchemy import  Column, Integer, Float, ForeignKey
from database import db

## Store
class MatrialCategory(db.Model):
    matrial_id = Column(Integer, ForeignKey('matrial.id'),  primary_key=True)
    category_id = Column(Integer, ForeignKey('category.id'),  primary_key=True)
    total_weight = Column(Float , nullable=False)
    km_price = Column(Float , nullable=False)
    km_points = Column(Float , nullable=False)
    def add(self):        
        db.session.add(self)
        db.session.commit()