#!/usr/bin/python3
""" Holds class History """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class History(BaseModel, Base):
    """ Representation of histories """
    __tablename__ = 'histories'
    p_ocular_hx = Column(String(128), nullable=False)
    p_medical_hx = Column(String(128), nullable=False)
    f_ocular_hx = Column(String(128), nullable=False)
    f_medical_hx = Column(String(128), nullable=False)
    patient_id = Column(String(60), ForeignKey('patients.id'), nullable=False)
    case_id = Column(String(60), ForeignKey('cases.id'), nullable=False)
