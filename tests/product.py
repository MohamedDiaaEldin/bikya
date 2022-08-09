
import sys
sys.path.append('..')
import unittest
from database import db
from main import app 

class ProductTest(unittest.TestCase):        
    # main setup
    def setUp(self) -> None:
        self.db = db        
        self.app = app                 
        self.client = self.app.test_client    

    def test_category_material(self):    
        response = self.client().get('/category_material_zone')
        self.assertEqual(response.status_code, 200)