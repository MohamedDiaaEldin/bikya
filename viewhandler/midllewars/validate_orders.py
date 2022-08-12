from flask import request

from viewhandler.utilities.request_handlers import bad_request

'''
    "category_id" : categoriesSelect.options[categoriesSelect.selectedIndex].value, 
    "matrial_id" : matrialsSelect.options[matrialsSelect.selectedIndex].value,
    "zone_id" : zonesSelect.options[zonesSelect.selectedIndex].value,
    "date" : dateInput.value,
    "time" : timeInput.value ,    
    "weight" : weightInput.value 
'''

# validate login request body
def validate_create_sell_request(f):    
    def is_valid_submit_sell(*args, **kwargs):
        body = request.get_json()        
        if not (body and body.get('category_id') and body.get('matrial_id') and body.get('zone_id') and body.get('date') and body.get('time') and body.get('weight')):
            return bad_request()
        return f(*args, **kwargs)
    return is_valid_submit_sell
'''
        "date": dateInput.value,
        "time": timeInput.value,
        "category_id": parseInt(categoriesSelect.options[categoriesSelect.selectedIndex].value),
        "matrial_id": parseInt(matrialsSelect.options[matrialsSelect.selectedIndex].value),
        "weight": parseInt(weightInput.value)
    
'''
def validate_create_buy_order(f):
    def is_valid(*args, **kwargs):
        body = request.get_json()        
        if not (body and body.get('category_id') and body.get('matrial_id') and body.get('weight') and body.get('date') and body.get('time')):
            return bad_request()
        return f(*args, **kwargs)
    return is_valid
