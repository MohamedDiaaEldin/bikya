from database import create_app 
from viewhandler.user_auth import user_auth_handler
from viewhandler.sell_orders import sell_order_handler

app = create_app() # configure app with database 

user_auth_handler(app)
sell_order_handler(app)