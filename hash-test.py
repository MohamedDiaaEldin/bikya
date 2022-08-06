import bcrypt

from modles.customers import Customer


def hash(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
def is_valid(password, hashed):
    print(type(password))
    print(type(hashed))
    # return bcrypt.checkpw(password.encode('utf-8'), hashed.decode('utf-8'))




