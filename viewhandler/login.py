
from flask import make_response, request
from viewhandler.utilities.jwt_generator import generate_jwt
from viewhandler.utilities.request_handlers import server_error, success_handler, unauthenticated_handler
from .midllewars.validate_user import  validate_rquest
from modles.customers import Customer

@validate_rquest
def login():
    try:        
        body = request.get_json()                
        customer = Customer.query.filter_by(email=body.get('email')).first()
        # customer = {'email':'ahmed', 'password' :'23'}
        if not (customer and body.get('password') == customer.password):
            return unauthenticated_handler()            
        res = make_response(success_handler())
        res.set_cookie('jwt', generate_jwt(body.get('email')))                
        return res
    except:
        return server_error()
    

def login_handler(app):
    app.route('/login', methods=['POST'])(login)
    