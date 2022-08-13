from flask import make_response
from database import create_app 
from viewhandler.user_auth import user_auth_handler
from viewhandler.product import sell_order_handler
from flask_cors import CORS

 
app = create_app() # configure app with database 
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:5500"}})

# flask_cors.corss_origin() 
# ["http:localhost:5500", "http://www.domain2.com"]
user_auth_handler(app)
sell_order_handler(app)


@app.route('/')
def set_cookie():
    res = make_response()        
        # set jwt in cookie
    res.set_cookie('jwt_test', '000000000000000')
    return res

