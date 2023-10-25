#!/usr/bin/python3
""" Contains the TestDBStorageDocs and TestDBStorage classes """

import unittest
import os
from models import storage
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


class TestDBStorage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set the environment to "testing"
        os.environ['CBASE_ENV'] = 'test'

    @classmethod
    def tearDownClass(cls):
        # Clean up after the test class
        del os.environ['CBASE_ENV']

    def test_case_model(self):
        # Test the Case model
        ncase = Case(patient_id="patient_id", optometrist_id="optometrist_id")
        storage.new(ncase)
        storage.save()
        retrieved_case = storage.get(Case, ncase.id)
        self.assertEqual(retrieved_case, ncase)

    def test_diagnosis_model(self):
        # Test the Diagnosis model
        new_diagnosis = Diagnosis(
            principal_diagnosis="principal_diagnosis",
            other_diagnosis_1="other_diagnosis_1",
            other_diagnosis_2="other_diagnosis_2",
            patient_id="patient_id",
            case_id="case_id"
        )
        storage.new(new_diagnosis)
        storage.save()
        retrieved_diagnosis = storage.get(Diagnosis, new_diagnosis.id)
        self.assertEqual(retrieved_diagnosis, new_diagnosis)

    def test_drug_model(self):
        # Test the Drug model
        ndrug = Drug(drug="drug", patient_id="patient_id", case_id="case_id")
        storage.new(ndrug)
        storage.save()
        retrieved_drug = storage.get(Drug, ndrug.id)
        self.assertEqual(retrieved_drug, ndrug)

    def test_examination_model(self):
        # Test the Examination model
        new_examination = Examination(
            visual_acuity="visual_acuity",
            ocular_exam="ocular_exam",
            chief_complaint="chief_complaint",
            on_direct_questions="on_direct_questions",
            iop="iop",
            blood_pressure="blood_pressure",
            patient_id="patient_id",
            case_id="case_id"
        )
        storage.new(new_examination)
        storage.save()
        retrieved_examination = storage.get(Examination, new_examination.id)
        self.assertEqual(retrieved_examination, new_examination)

    def test_history_model(self):
        # Test the History model
        new_history = History(
            p_ocular_hx="p_ocular_hx",
            p_medical_hx="p_medical_hx",
            f_ocular_hx="f_ocular_hx",
            f_medical_hx="f_medical_hx",
            patient_id="patient_id",
            case_id="case_id"
        )
        storage.new(new_history)
        storage.save()
        retrieved_history = storage.get(History, new_history.id)
        self.assertEqual(retrieved_history, new_history)

    def test_lens_model(self):
        # Test the Lens model
        nlens = Lens(lens_rx="lens_rx", patient_id="patient_id", case_id="case_id")
        storage.new(nlens)
        storage.save()
        retrieved_lens = storage.get(Lens, nlens.id)
        self.assertEqual(retrieved_lens, nlens)

    def test_optometrist_model(self):
        # Test the Optometrist model
        new_optometrist = Optometrist(
            name="optometrist_name",
            email="optometrist_email",
            password="optometrist_password",
            license="optometrist_license"
        )
        storage.new(new_optometrist)
        storage.save()
        retrieved_optometrist = storage.get(Optometrist, new_optometrist.id)
        self.assertEqual(retrieved_optometrist, new_optometrist)

    def test_patient_model(self):
        # Test the Patient model
        new_patient = Patient(
            firstname="patient_firstname",
            surname="patient_surname",
            dob="patient_dob",
            tel="patient_tel",
            occupation="patient_occupation",
            insurance="patient_insurance"
        )
        storage.new(new_patient)
        storage.save()
        retrieved_patient = storage.get(Patient, new_patient.id)
        self.assertEqual(retrieved_patient, new_patient)

    def test_receptionist_model(self):
        # Test the Receptionist model
        new_receptionist = Receptionist(
            name="receptionist_name",
            email="receptionist_email",
            password="receptionist_password"
        )
        storage.new(new_receptionist)
        storage.save()
        retrieved_receptionist = storage.get(Receptionist, new_receptionist.id)
        self.assertEqual(retrieved_receptionist, new_receptionist)

    def test_test_model(self):
        # Test the Test model
        new_test = Test(
            retinoscopy="retinoscopy",
            autorefraction="autorefraction",
            sudjective_refraction="sudjective_refraction",
            other_tests="other_tests",
            patient_id="patient_id",
            case_id="case_id"
        )
        storage.new(new_test)
        storage.save()
        retrieved_test = storage.get(Test, new_test.id)
        self.assertEqual(retrieved_test, new_test)

    def test_count_method(self):
        # Test the 'count' method for various models
        count_cases = storage.count(Case)
        count_diagnoses = storage.count(Diagnosis)
        count_drugs = storage.count(Drug)
        count_examinations = storage.count(Examination)
        count_histories = storage.count(History)
        count_lenses = storage.count(Lens)
        count_optometrists = storage.count(Optometrist)
        count_patients = storage.count(Patient)
        count_receptionists = storage.count(Receptionist)
        count_tests = storage.count(Test)
        self.assertEqual(count_cases, 1)
        self.assertEqual(count_diagnoses, 1)
        self.assertEqual(count_drugs, 1)
        self.assertEqual(count_examinations, 1)
        self.assertEqual(count_histories, 1)
        self.assertEqual(count_lenses, 1)
        self.assertEqual(count_optometrists, 1)
        self.assertEqual(count_patients, 1)
        self.assertEqual(count_receptionists, 1)
        self.assertEqual(count_tests, 1)

    def test_drop_all_tables(self):
        # Test that tables are dropped in the testing environment
        # Ensure no tables are present
        self.assertEqual(storage.count(Case), 0)
        self.assertEqual(storage.count(Diagnosis), 0)
        self.assertEqual(storage.count(Drug), 0)
        self.assertEqual(storage.count(Examination), 0)
        self.assertEqual(storage.count(History), 0)
        self.assertEqual(storage.count(Lens), 0)
        self.assertEqual(storage.count(Optometrist), 0)
        self.assertEqual(storage.count(Patient), 0)
        self.assertEqual(storage.count(Receptionist), 0)
        self.assertEqual(storage.count(Test), 0)


if __name__ == "__main__":
    unittest.main()
