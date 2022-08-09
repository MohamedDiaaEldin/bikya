
import sys
sys.path.append('..')
import unittest
import json
from database import db
from main import app 
import random

def makeCustomer():       
        rand = random.randint(5, 1000)
        customer = {
            "first_name":"mohamed",
            "last_name": "diaa",
            "email":     f"{rand}@gmail.com", 
            "phone":  "01233333",
            "address":"6th of october city",
            "password":"123456"
        }
        return customer
    
class CustomerTest(unittest.TestCase):
    
    
    customer  = makeCustomer()
         
    # main setup
    def setUp(self) -> None:
        self.db = db        
        self.app = app                 
        self.client = self.app.test_client
    
  

    def test_signup(self):    
        # self.customer = self.makeCustomer()
        response = self.client().post('/signup', 
                       data=json.dumps(CustomerTest.customer),
                       content_type='application/json')            
        self.assertEqual(response.status_code, 200)
        
    

    # def test_login(self):        
    #     customer_data = {
    #         'email' : Login.customer.get('email'),
    #         'password' :Login.customer.get('password')
    #     }
    #     response = self.client().post('/login', 
    #                    data=json.dumps(customer_data),
    #                    content_type='application/json')        
        
    #     self.assertEqual(response.status_code, 200)

def start():
    loader = unittest.TestLoader()
    loader.sortTestMethodsUsing = None
    unittest.main(testLoader=loader)

    