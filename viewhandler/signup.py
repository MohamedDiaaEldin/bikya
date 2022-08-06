
from flask import request
from modles.customers import Customer
from viewhandler.midllewars.validate_user import validate_signup_request
from .utilities import pass_hash
from .utilities.request_handlers import success_handler, conflict_request



@validate_signup_request
def create_user():
    body = request.get_json()    
    ## if user signup 
    if Customer.query.filter_by(email=body.get('email')).first() :
        return conflict_request()
    
    
    # hash password
    hashed = pass_hash.hash_string(body.get('password'))        
    
    # create new customer
    customer = Customer(first_name=body.get('first_name'), last_name=body.get('last_name'), email=body.get('email'), password=hashed, address=body.get('address'), phone=body.get('phone'), points=0)
    customer.add()    
    
    return success_handler()


def signup_handler(app):
    app.route('/signup', methods=['POST'])(create_user)
   
    