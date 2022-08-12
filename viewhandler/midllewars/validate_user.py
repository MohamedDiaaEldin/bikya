from functools import wraps
from flask import  request
from viewhandler.utilities.request_handlers import bad_request, unauthenticated_handler
from ..utilities.jwt_generator import is_valid_jwt


# validate login request body
def validate_login_request(f):    
    def is_valid_login_data(*args, **kwargs):
        body = request.get_json()        
        if not (body and body.get('email') and body.get('password') ):
            return bad_request()
        
        return f(*args, **kwargs)
    return is_valid_login_data


# validate signup request body
def validate_signup_request(f):        
    def is_valid_signup_data(*args, **kwargs):
        body = request.get_json()
        if not (body and body.get('first_name') and body.get('last_name') and body.get('email') and body.get('password') and body.get('address') and body.get('phone')):
            return bad_request()
        return f(*args, **kwargs)
    return is_valid_signup_data




# jwt authentication 
def authenticate(f):   
    print('in auth----->' , __name__)       
    @wraps(f)
    def is_authenticated(*args, **kwargs):
        user_jwt = request.cookies.get('jwt')
        if not (user_jwt and is_valid_jwt(user_jwt)):
            return unauthenticated_handler()        
        return f(*args, **kwargs)
    return is_authenticated
