from flask import make_response, request
from modles.customers import Customer
from ..utilities.jwt_generator import generate_jwt


def validate_rquest(f):    
    def is_valid_login_data(*args, **kwargs):
        body = request.get_json()        
        if not (body and body.get('email') and body.get('password') ):
            return 'bad request'
        
        return f(*args, **kwargs)
    return is_valid_login_data


def authenticate(f):
    @validate_rquest        
    def decorated_function(*args, **kwargs):        
        # select customer with it's email 
        # compare passowrd and email 
        # if valid :
        #   generate jwt 
        #   set jwt into cookies        
        # else:
        #   return 'unauthenticated ' 
        
        if request.get_json().get('name') != 'ahmed':            
            return '401 not authenticated'
        else:            
            res = make_response()
            res.set_cookie('jwt', generate_jwt(request.get_json().get('name')))                
            return res
        return f(*args, **kwargs)
    return decorated_function
