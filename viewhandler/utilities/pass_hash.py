import bcrypt


password = b'mypasswodrd'


def hash_string(password):    
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
def is_valid(password, hashed):        
    return True  if bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8')) else False
