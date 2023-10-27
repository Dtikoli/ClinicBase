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
