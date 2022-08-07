
import sys
sys.path.append('..')
import unittest
import json
from database import db
from main import app 
import random

def makeCustomer():       
        print('in make customer-------------------_>')
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
    
class Login(unittest.TestCase):
    
    
    customer  = makeCustomer()
        
    # @classmethod
    # def setUpClass(self):                
    #     print('in set up class-------------------_>')
    #     self.customer = self.makeCustomer()
        
    # main setup
    def setUp(self) -> None:
        print('in set up-------------------_>')
        self.db = db        
        # self.app = create_app()
        self.app = app                 
        self.client = self.app.test_client
    
  

    def test_signup(self):    
        # self.customer = self.makeCustomer()
        print('in sigin up-------------------_>')
        response = self.client().post('/signup', 
                       data=json.dumps(Login.customer),
                       content_type='application/json')            
        self.assertEqual(response.status_code, 200)
        
    

    def test_login(self):        
        print('in login -------------------_>')
    
        self.data = {
            # 'email' : Login.customer.get('email'),
            'email' : Login.customer.get('email'),
            'password' :Login.customer.get('password')
            # 'password' :  Login.customer.get('password')
        }
        print('data ---> ', self.data )
        response = self.client().post('/login', 
                       data=json.dumps(self.data),
                       content_type='application/json')        
        
        print('data ---> ', self.data )
        self.assertEqual(response.status_code, 200)


# def start():
#     unittest.main()

def start():
    loader = unittest.TestLoader()
    loader.sortTestMethodsUsing = None
    unittest.main(testLoader=loader)

    