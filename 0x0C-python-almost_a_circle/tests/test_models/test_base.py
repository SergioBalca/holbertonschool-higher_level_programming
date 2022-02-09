#!/usr/bin/python3

from models.base import Base
import unittest
import pycodestyle

from models.rectangle import Rectangle

"""module that contains unittests for Base class"""

"""TestBase class that inherits from unittest.Testcase class"""


class TestBase(unittest.TestCase):

    def test_pep8(self):

        """checks pep8 style guide on every file"""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        msg = "Found code style error (and warnings)."
        self.assertEqual(result.total_errors, 0, msg)

    def test_id(self):

        """checks if Base handles id's correctly"""

        base_1 = Base(3)
        base_2 = Base()
        base_3 = Base(-2)
        base_4 = Base()

        self.assertEqual(base_1.id, 3)
        self.assertEqual(base_2.id, 1)
        self.assertEqual(base_3.id, -2)
        self.assertEqual(base_4.id, 2)

    def test_to_json_string(self):

        "Test for to_json_string method"

        r_1 = Rectangle(10, 7, 2, 8, 6)
        dict_r1 = r_1.to_dictionary()
        result = '[{"id": 6, "width": 10, "height": 7, "x": 2, "y": 8}]'

        self.assertEqual(Base.to_json_string([dict_r1]), result)
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string(None), "[]")
