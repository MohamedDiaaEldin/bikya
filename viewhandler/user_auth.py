
from flask import make_response, request
from viewhandler.utilities.jwt_generator import generate_jwt # jwt
from .utilities import pass_hash # password hashing
from viewhandler.utilities.request_handlers import server_error, success_handler, unauthenticated_handler, conflict_request # rerver error messages
from .midllewars.validate_user import  validate_login_request,validate_signup_request # validate request body - decorator 
from modles.customers import Customer # Cutomer model


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


@validate_login_request
def user_login():
    try:
        # extract data from request        
        body = request.get_json()                
        # get user data        
        customer = Customer.query.filter_by(email=body.get('email')).first()        
        
        # validate user credentials
        if not (customer and  pass_hash.is_valid(body.get('password') , customer.password) ):            
            return unauthenticated_handler()            
        
        res = make_response(success_handler())        
        # set jwt in cookie
        res.set_cookie('jwt', generate_jwt(body.get('email')))
        
        return res
    except:
        return server_error()



def user_auth_handler(app):
    app.route('/login', methods=['POST'])(user_login)
    app.route('/signup', methods=['POST'])(create_user)
    