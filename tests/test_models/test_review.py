#!/usr/bin/python3
""" Module to test cases """
from datetime import datetime
from models.review import Review
import unittest
import pep8


class TestCityClass(unittest.TestCase):
    """ Unit test class for Base User class """

    def test_pep8(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/user.py"])
        self.assertEqual(result.total_errors, 0)

    @classmethod
    def setUpClass(cls):
        """ set up instances for all tests """
        cls.review = Review()

    def test_created_at(self):
        """ Test created_at """
        self.assertEqual(datetime, type(self.review.created_at))

    def test_updated_at(self):
        """ Test updated_at """
        self.assertEqual(datetime, type(self.review.updated_at))

    def test_user_id(self):
        """ Test user_id is string and is empty """
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertEqual(self.review.user_id, "")

    def test_place_id(self):
        """ Test place_id is string and is empty """
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertEqual(self.review.place_id, "")
    def test_text(self):
        """ Test text is string and is empty """
        self.assertTrue(hasattr(self.review, "text"))
        self.assertEqual(self.review.text, "")


if __name__ == "__main__":
    unittest.main()
