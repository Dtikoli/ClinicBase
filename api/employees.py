#!/usr/bin/python3
""" API eployees speficic routes """

from api import bp_api
from flask import abort, jsonify, request
from flask_cors import cross_origin
from models.optometrist import Optometrist
from models.receptionist import Receptionist
from models import storage

dbsession = storage._DBStorage__session


@bp_api.route('/get_employee/<employee_id>', strict_slashes=False)
@cross_origin(origins=["127.0.0.1"])
def get_employee(employee_id):
    """ Returns employee's updated information """
    employee = dbsession.query(Receptionist).get(employee_id)
    if not employee:
        employee = dbsession.query(Optometrist).get(employee_id)    
    if not employee:
        abort(404)
    return jsonify(employee.to_dict())


@bp_api.route('/employee', methods=['POST'], strict_slashes=False)
@cross_origin(origins=["127.0.0.1"])
def post_employee():
    """ Creates a new employee """
    if not request.is_json:
        abort(400, description="Not a JSON")
    data = request.get_json()
    if 'name' not in data:
        abort(400, description="Missing name")
    if 'email' not in data:
        abort(400, description="Missing email")
    if 'password' not in data:
        abort(400, description="Missing password")
    if 'license' in data:
        employee = Optometrist(**data)
    else:
        employee = Receptionist(**data)
    storage.add(employee)
    storage.save()
    return jsonify(employee.to_dict()), 201


@bp_api.route('/patients/<patient_id>', methods=['PUT'], strict_slashes=False)
@cross_origin(origins=["127.0.0.1"])
def put_patient(patient_id):
    """ Updates a patient information """
    patient = storage.get(Patient, patient_id)
    if not patient:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'firstname', 'surname', 'dob', 'created_at', 'updated']
    for key, value in request.get_json().items():
        if key not in ignore:
            setattr(patient, key, value)
    storage.save()
    return jsonify(patient.to_dict()), 200
