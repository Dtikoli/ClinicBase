#!/usr/bin/python3
""" Holds class Diagnoses """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Text


class Diagnosis(BaseModel, Base):
    """ Representation of diagnoses """
    __tablename__ = 'diagnoses'
    principal = Column(Text, nullable=False)
    other1 = Column(Text)
    other2 = Column(Text)
    patient_id = Column(String(60), ForeignKey('patients.id'), nullable=False)
    case_id = Column(String(60), ForeignKey('cases.id'), nullable=False)
