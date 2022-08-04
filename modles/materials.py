import sys
sys.path.append('..')
from sqlalchemy import  Column, String, Integer
from sqlalchemy.orm import relationship

from database import db


class Matrial(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    # matrialCategories = relationship("MatrialCategory")
    # buy_orders = relationship("BuyCategoryMatrial")
    # sell_orders = relationship("SellCategorymatrial")
   
    def add(self):        
        db.session.add(self)
        db.session.commit()