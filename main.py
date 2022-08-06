from flask import jsonify, make_response, request
from database import create_app
from modles.customers import Customer
from viewhandler.login import login_handler
from viewhandler.signup import signup_handler

app = create_app()


@app.route('/clear')
def clear():
    res = make_response()
    res.set_cookie('jwt', '', expires=0)
    return res
    
@app.route('/')
def index():
    res = make_response(jsonify({'name':'ad'}),200)        
    # print(request.cookies.get('jwt'))
    # res.set_cookie('jwt','dadfjsfhkasn')    
    # print(Customer.query.all())
    return res
    
login_handler(app)
signup_handler(app)