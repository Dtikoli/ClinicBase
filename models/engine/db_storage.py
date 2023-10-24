#!/usr/bin/python3
""" Contains the class DBStorage """

from models import storage
from models.base_model import Base
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
from os import getenv
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"Case": Case, "Diagnosis": Diagnosis, "Drug": Drug,
           "Test": Test, "Examination": Examination, "History": History,
           "Lens": Lens, "Optometrist": Optometrist, "Patient": Patient,
           "Receptionist": Receptionist}

load_dotenv()


class DBStorage:
    """interacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        if getenv('HBNB_ENV') == 'test':
            db_uri = getenv('TEST_DATABASE_URI')
            Base.metadata.drop_all(self.__engine)

        else:
            db_uri = getenv('DEV_DATABASE_URI')

        self.__engine = create_engine(db_uri, pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.close()

    def get(self, cls, id):
        """ Returns the object based on the class name and its ID """
        if cls not in classes.values():
            return None
        all_cls = storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value
        return None

    def count(self, cls=None):
        """ count the number of objects in storage """
        all_class = classes.values()
        if not cls:
            count = 0
            for clas in all_class:
                count += len(storage.all(clas).values())
        else:
            count = len(storage.all(cls).values())
        return count
