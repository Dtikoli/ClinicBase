#!/usr/bin/python3
""" Contains the TestDBStorageDocs and TestDBStorage classes """

import unittest
from models import storage
from models.user import User
from models.city import City
from models.state import State


class TestDBStorage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set the environment to "testing"
        import os
        os.environ['HBNB_ENV'] = 'test'

    @classmethod
    def tearDownClass(cls):
        # Clean up after the test class
        del os.environ['HBNB_ENV']

    def test_all_method(self):
        # Test the 'all' method
        all_users = storage.all(User)
        all_cities = storage.all(City)
        all_states = storage.all(State)

        self.assertEqual(type(all_users), dict)
        self.assertEqual(type(all_cities), dict)
        self.assertEqual(type(all_states), dict)

    def test_new_and_save_methods(self):
        # Test the 'new' and 'save' methods
        new_user = User(email="test@example.com", password="password")
        new_city = City(name="Test City")

        # Add objects and save
        storage.new(new_user)
        storage.new(new_city)
        storage.save()

        # Check if objects are in the database
        retrieved_user = storage.get(User, new_user.id)
        retrieved_city = storage.get(City, new_city.id)

        self.assertIsNotNone(retrieved_user)
        self.assertIsNotNone(retrieved_city)

    def test_delete_method(self):
        # Test the 'delete' method
        new_state = State(name="Test State")
        storage.new(new_state)
        storage.save()

        # Delete the state
        storage.delete(new_state)
        storage.save()

        # Check if the state is no longer in the database
        retrieved_state = storage.get(State, new_state.id)
        self.assertIsNone(retrieved_state)

    def test_get_method(self):
        # Test the 'get' method
        new_user = User(email="test@example.com", password="password")
        storage.new(new_user)
        storage.save()

        # Retrieve the user
        retrieved_user = storage.get(User, new_user.id)
        self.assertEqual(retrieved_user, new_user)

    def test_count_method(self):
        # Test the 'count' method
        count_users = storage.count(User)
        count_cities = storage.count(City)
        count_states = storage.count(State)

        self.assertEqual(count_users, 1)
        self.assertEqual(count_cities, 1)
        self.assertEqual(count_states, 0)  # State object was deleted

    def test_drop_all_tables(self):
        # Test that tables are dropped in the testing environment
        # Ensure no tables are present
        self.assertEqual(storage.count(User), 0)
        self.assertEqual(storage.count(City), 0)
        self.assertEqual(storage.count(State), 0)


if __name__ == "__main__":
    unittest.main()
