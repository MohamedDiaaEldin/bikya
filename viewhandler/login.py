
from flask import make_response, request
from viewhandler.utilities.jwt_generator import generate_jwt
from viewhandler.utilities.request_handlers import server_error, success_handler, unauthenticated_handler
from .midllewars.validate_user import  authenticate, validate_login_request
from modles.customers import Customer
from .utilities.pass_hash import is_valid


@validate_login_request
def login():
    try:
        # extract data from request        
        body = request.get_json()                
        
        # get user data        
        customer = Customer.query.filter_by(email=body.get('email')).first()        
        
        # validate user credentials
        if not (customer and  is_valid(body.get('password') , customer.password) ):            
            return unauthenticated_handler()            
        
        res = make_response(success_handler())
        res.set_cookie('jwt', generate_jwt(body.get('email')))
        return res
    except:
        return server_error()

@authenticate
def test():
    return 'hi'

def login_handler(app):
    app.route('/login', methods=['POST'])(login)
    app.route('/test', methods=['POST'])(test)
    