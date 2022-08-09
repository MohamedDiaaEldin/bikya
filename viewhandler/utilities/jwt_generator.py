import jwt 

def generate_jwt(payload):
    return jwt.encode({'email':payload}, "secret", algorithm="HS256")


def is_valid_jwt(token):
    try:
        jwt.decode(token, 'secret' , algorithms="HS256")
        return True
    except:
        return False
    
def decode_jwt(token):
    try:
        return jwt.decode(token, 'secret', algorithms='HS256')
    except:
        return None