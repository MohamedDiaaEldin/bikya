
from http import cookies
import sys
sys.path.append('..')
import unittest
from database import db
from main import app 
import json

class ProductTest(unittest.TestCase):        
    # main setup
    def setUp(self) -> None:
        self.db = db        
        self.app = app                 
        self.client = self.app.test_client    

    def test_category_material(self):    
        response = self.client().get('/category_material_zone')
        self.assertEqual(response.status_code, 200)
    
    def test_make_sell_order(self):
        sell_order_info = {
            "category_id" : 1, 
            "matrial_id" : 2,
            "zone_id" : 1,
            "date" : "20-10-2020",
            "time" : "12:44",    
            "weight" : "100" 
            }
        # make respose with correct data
        # without authentication 
        response = self.client().post('/sell_order', 
                       data=json.dumps(sell_order_info),
                       content_type='application/json')
        
        self.assertEqual(response.status_code, 401)
        
     
        
        