#!/usr/bin/python3
""" Module to test cases """
from datetime import datetime
from models.user import User
import unittest
import pep8


class TestUserClass(unittest.TestCase):
    """ Unit test class for Base User class """

    def test_pep8(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/user.py"])
        self.assertEqual(result.total_errors, 0)

    @classmethod
    def setUpClass(cls):
        """ set up instances for all tests """
        cls.user = User()

    def test_created_at(self):
        """ Test created_at """
        self.assertEqual(datetime, type(self.user.created_at))

    def test_updated_at(self):
        """ Test updated_at """
        self.assertEqual(datetime, type(self.user.updated_at))

    def test_string(self):
        """ Test for __str__ method """
        good = "[User] ({}) {}".format(self.user.id, self.user.__dict__)
        self.assertEqual(good, str(self.user))


if __name__ == "__main__":
    unittest.main()
