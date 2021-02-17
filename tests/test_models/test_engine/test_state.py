#!/usr/bin/python3
""" Module to test cases """
from datetime import datetime
from models.state import State
import unittest
import pep8


class TestStateClass(unittest.TestCase):
    """ Unit test class for Base User class """

    def test_pep8(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/user.py"])
        self.assertEqual(result.total_errors, 0)

    @classmethod
    def setUpClass(cls):
        """ set up instances for all tests """
        cls.state = State()

    def test_created_at(self):
        """ Test created_at """
        self.assertEqual(datetime, type(self.state.created_at))

    def test_updated_at(self):
        """ Test updated_at """
        self.assertEqual(datetime, type(self.state.updated_at))

    def test_name(self):
        """ Test name is string and is empty """
        self.assertTrue(hasattr(self.state, "name"))
        self.assertEqual(self.state.name, "")


if __name__ == "__main__":
    unittest.main()
