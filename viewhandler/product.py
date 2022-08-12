
from flask import jsonify, request
from modles.categories import Category
from modles.materials import Matrial
from modles.customers import Customer
from modles.delivery import Delivery
from modles.sell_categories_materials import SellCategorymatrial
from modles.matrials_categories import MatrialCategory
from modles.zone import Zone
from viewhandler.utilities.request_handlers import server_error, success_handler, unauthenticated_handler
from .utilities.data_factory import  categories_material_zone
from .midllewars.validate_orders import validate_create_sell_request, validate_create_buy_order
from .utilities.jwt_generator import decode_jwt

from .midllewars.validate_user import authenticate
    
print('current name is ', __name__)
def get_category_material_zone():
    try:        
        categories = Category.query.all()
        materials = Matrial.query.all()
        zones = Zone.query.all()
        return jsonify(categories_material_zone(categories=categories, materials=materials, zones=zones)), 200
    except:
        return server_error()


@authenticate
@validate_create_sell_request
def create_sell_order():
    try:        
        customer_email = decode_jwt(request.cookies.get('jwt')).get('email')
        customer = Customer.query.filter_by(email=customer_email).first()
        if not customer:
            return unauthenticated_handler()
        
        body =  request.get_json()    
        # get product with choosen data
        category_matrial = MatrialCategory.query.filter_by(matrial_id=body.get('matrial_id'), category_id=body.get('category_id')).first()            
       
        # calculate km points
        points = float(body.get('weight')) * category_matrial.km_points
        
        ## select delivery with order 
        selected_delivery = Delivery.query.filter_by(zone_id=int(body.get('zone_id'))).first()

        ## insert sell order 
        sell_category_matrial = SellCategorymatrial(matrial_id=int(body.get('matrial_id')), category_id=int(body.get('category_id')) , delivery_id=selected_delivery.id, customer_id=customer.id, date=body.get('date'), time=body.get('time'), weight=float(body.get('weight')), points=points, done=False)
        sell_category_matrial.add()
        
        return success_handler()
    except:
        return server_error()
    
    
@authenticate
@validate_create_buy_order
def check_weight():
    # check if ordered weight is there
    # return True and price if there eles return 404
    return 'hi'    

def sell_order_handler(app):
    app.route('/category_material_zone')(get_category_material_zone)
    app.route('/sell_order', methods=['POST'])(create_sell_order)
    app.route('/check_weight', methods=['POST'])(check_weight)
    

