#!/usr/bin/python3
""" Module to test cases """
from datetime import datetime
from models.city import City
import unittest
import pep8


class TestCityClass(unittest.TestCase):
    """ Unit test class for City class """

    def test_pep8(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/user.py"])
        self.assertEqual(result.total_errors, 0)

    @classmethod
    def setUpClass(cls):
        """ set up instances for all tests """
        cls.city = City()

    def test_created_at(self):
        """ Test created_at """
        self.assertEqual(datetime, type(self.city.created_at))

    def test_updated_at(self):
        """ Test updated_at """
        self.assertEqual(datetime, type(self.city.updated_at))

    def test_name(self):
        """ Test name is string and is empty """
        self.assertTrue(hasattr(self.city, "name"))
        self.assertEqual(self.city.name, "")

    def test_state_id(self):
        """ Test id is string and is empty """
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertEqual(self.city.state_id, "")


if __name__ == "__main__":
    unittest.main()
