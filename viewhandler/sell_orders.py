
from flask import jsonify
from modles.categories import Category
from modles.materials import Matrial
from .utilities.data_factory import categories_material

def get_category_material():
    categories = Category.query.all()
    materials = Matrial.query.all()
    return jsonify(categories_material(categories=categories, materials=materials)), 200
    


def sell_order_handler(app):
    app.route('/category_material')(get_category_material)
    
