#!/usr/bin/python3

""" Module to test cases """
from datetime import datetime
from models.base_model import BaseModel
import unittest
import pep8


class TestBaseModel(unittest.TestCase):
    """ Unit test class for Base Model class """

    def test_pep8(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/base_model.py"])
        self.assertEqual(result.total_errors, 0)

    def test_created_at(self):
        self.assertEqual(datetime, type(self.basemodel.created_at))

    def test_updated_at(self):
        self.assertEqual(datetime, type(self.basemodel.updated_at))


if __name__ == "__main__":
    unittest.main()
