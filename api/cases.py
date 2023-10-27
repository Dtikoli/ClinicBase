#!/usr/bin/python3
""" API cases routes """

from api import bp_api
from flask import abort, jsonify, request
from flask_cors import cross_origin
from datetime import date
from models.case import Case
from models.diagnosis import Diagnosis
from models.drug import Drug
from models.examination import Examination
from models.history import History
from models.lens import Lens
from models.optometrist import Optometrist
from models.patient import Patient
from models.receptionist import Receptionist
from models.test import Test
from models import storage

dbsession = storage._DBStorage__session


@bp_api.route('/status', methods=['GET'], strict_slashes=False)
@cross_origin(origins=["127.0.0.1"])
def status():
    """ Status of API """
    return jsonify({"status": "OK"})


@bp_api.route('/patient_count', methods=['POST'], strict_slashes=False)
@cross_origin(origins=["127.0.0.1"])
def patient_count():
    """ Returns the number of patients within a specified time """
    if not request.get_json():
        abort(400, description="Not a JSON")

    data = request.get_json()
    start_date = data.get('start_date', date.min)
    end_date = data.get('end_date', date.today())
    patient_count = session.query(Patient)\
        .filter(Patient.update_at.between(start_date, end_date)).count()

    return jsonify({'patient_count': patient_count})


@bp_api.route('/case_count', methods=['POST'], strict_slashes=False)
@cross_origin(origins=["127.0.0.1"])
def case_count():
    """ Returns the number of cases within a specified time """
    if not request.get_json():
        abort(400, description="Not a JSON")

    data = request.get_json()
    start_date = data.get('start_date', date.min)
    end_date = data.get('end_date', date.today())
    case_count = session.query(Case)\
        .filter(Case.update_at.between(start_date, end_date)).count()

    return jsonify({'case_count': case_count})
