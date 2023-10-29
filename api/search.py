#!/usr/bin/python3
""" API search routes """

from api import bp_api
from flask import abort, jsonify, request
from flask_cors import cross_origin
from models.optometrist import Optometrist
from models.receptionist import Receptionist
from models.patient import Patient
from models.engine.db_storage import DBStorage

db_storage = DBStorage()
session = db_storage.reload()


@bp_api.route('/patients/search', methods=['POST'], strict_slashes=False)
@cross_origin(origins=["127.0.0.1"])
def search_patients():
    """" Handles patient search """
    if not request.get_json():
        abort(400, description="Not a JSON")

    data = request.get_json()
    insurance = data.get('insurance')
    firstname = data.get('firstname')
    surname = data.get('surname')

    base_query = Patient.query
    if insurance:
        base_query = base_query\
            .filter(Patient.insurance.ilike(f'%{insurance}%'))

    if firstname:
        base_query = base_query\
            .filter(Patient.firstname.ilike(f'%{firstname}%'))

    if surname:
        base_query = base_query\
            .filter(Patient.surname.ilike(f'%{surname}%'))

    filtered_patients = base_query.all()
    return jsonify([patient.to_dict() for patient in filtered_patients])


@bp_api.route('/employees/search', methods=['POST'], strict_slashes=False)
@cross_origin(origins=["127.0.0.1"])
def search_employees():
    """" Handles employee search """
    if not request.get_json():
        abort(400, description="Not a JSON")

    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    receptionist_query = session.query(Receptionist)
    optometrist_query = session.query(Optometrist)

    if name:
        receptionist_results = receptionist_query\
            .filter(Receptionist.name.ilike(f'%{name}%')).all()
        optometrist_results = optometrist_query\
            .filter(Optometrist.name.ilike(f'%{name}%')).all()
    else:
        receptionist_results = receptionist_query.all()
        optometrist_results = optometrist_query.all()

    if email:
        receptionist_results = [
            r for r in receptionist_results
            if r.email.lower().find(email.lower()) != -1
        ]

        optometrist_results = [
            o for o in optometrist_results
            if o.email.lower().find(email.lower()) != -1
        ]

    result_dicts = []

    for receptionist in receptionist_results:
        result_dicts.append(receptionist.to_dict())

    for optometrist in optometrist_results:
        result_dicts.append(optometrist.to_dict())

    return jsonify(result_dicts)
