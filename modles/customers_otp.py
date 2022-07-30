import sys
sys.path.append('..')
from sqlalchemy import  Column, String
from database import db

class Customer_OTP(db.Model):
    __tablename__ = 'customer_otp'
    email = Column(String, primary_key=True)
    otp = Column(String, nullable=False)

