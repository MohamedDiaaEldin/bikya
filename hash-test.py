import bcrypt

password = b'mypasswodrd'


hashed = bcrypt.hashpw(password, bcrypt.gensalt())


hashed = b'$2b$12$l9yAOeOJ3B/5OvFRXlD7Xu0mjOk8sK1QenDmf2dRDU0z7aNLA0jIS'
if bcrypt.checkpw(password, hashed):
    print('yes')
else:
    print('no')