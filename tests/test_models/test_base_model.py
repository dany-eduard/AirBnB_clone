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

    @classmethod
    def setUpClass(cls):
        """ set up instances for all tests """
        cls.basemodel = BaseModel()

    def test_created_at(self):
        """ Test created_at """
        self.assertEqual(datetime, type(self.basemodel.created_at))

    def test_updated_at(self):
        """ Test updated_at """
        self.assertEqual(datetime, type(self.basemodel.updated_at))

    def test_id_type(self):
        """ Test for type id """
        self.assertEqual(str, type(self.basemodel.id))

    def test_to_dict(self):
        """ Test to_dict """
        my_dict = self.basemodel.to_dict()
        self.assertEqual(dict, type(my_dict))
        self.assertTrue("to_dict" in dir(self.basemodel))

    def test_class_doc(self):
        """ Test for class documentation """
        self.assertTrue(len(BaseModel.__doc__) > 0)

    def test_method_docs(self):
        """ Test for method documentation """
        for method in dir(BaseModel):
            self.assertTrue(len(method.__doc__) > 0)


if __name__ == "__main__":
    unittest.main()
