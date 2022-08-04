

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