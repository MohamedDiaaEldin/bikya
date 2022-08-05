
from flask import request
from modles.customers import Customer
from viewhandler.midllewars.validate_user import validate_signup_request




@validate_signup_request
def create():
    print(request.get_json())
    # hash password
    # add user to database
    return 'hi'


def signup_handler(app):
    app.route('/signup', methods=['POST'])(create)
    