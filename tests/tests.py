import sys
sys.path.append('..')
import unittest
import json
# from main import app
from database import db
from main import app 

class BikyaTest(unittest.TestCase):
    def setUp(self) -> None:
        self.db = db        
        # self.app = create_app()
        self.app = app 

        self.client = self.app.test_client
            
        # return super().setUp()

    def test_lib(self):
        res = self.client().get('/user')            
        data = json.loads(res.data)
        print(data)
        self.assertEqual(res.status_code, 200)
        
# from auth.EndpointTest import EndPointsTest

def start():
    unittest.main()
if __name__ == "__main__":
    unittest.main()