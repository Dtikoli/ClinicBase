#!/usr/bin/python3
""" Flask Application API """

from flask import Blueprint, make_response, jsonify

bp_api = Blueprint('api', __name__, url_prefix='/api')


@bp_api.errorhandler(404)
def not_found(error):
    """ 404 Error """
    return make_response(jsonify({'error': "Not found"}), 404)

from api import route1 *
