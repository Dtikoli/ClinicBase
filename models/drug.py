#!/usr/bin/python3
""" Holds class Drug """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class Drug(BaseModel, Base):
    """ Representation of drugs """
    __tablename__ = 'drugs'
    principal_drug = Column(String(128), nullable=False)
    other_drug_1 = Column(String(128))
    other_drug_2 = Column(String(128))
    patient_id = Column(String(60), ForeignKey('patients.id'), nullable=False)
    case_id = Column(String(60), ForeignKey('cases.id'), nullable=False)
