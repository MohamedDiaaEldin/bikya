import sys
sys.path.append('..')
from sqlalchemy import  Column, String, Integer
from database import db

class Zone(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
      