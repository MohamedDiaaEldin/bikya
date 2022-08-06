

from flask import jsonify

def server_error(message='server error'):
    return jsonify({
        'message':message
    }), 500
    
def unauthenticated_handler(message='unauthenticated user'):
    return jsonify({
    'message':message
}), 401
    
def success_handler(message='ok'):
    return jsonify({
    'message':message
}), 200
    
def bad_request(message='bad request'):
    return jsonify({
    'message':message
}), 400
    
def conflict_request(message='confilct'):
    return jsonify({
    'message':message
}), 409