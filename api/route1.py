#!/usr/bin/python3
""" Flask Application API """

from flask import Blueprint, make_response, jsonify
from flask_cors import cross_origin

bp_api = Blueprint('api', __name__, url_prefix='/api')

# Apply the cross_origin decorator to specific routes within the Blueprint
@bp_api.route('/your_route')
@cross_origin(origins=["https://example.com", "https://anotherdomain.com"])
def your_route_function():
    # Your route logic here
    pass
