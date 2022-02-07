#!/usr/bin/python3

from models.base import Base
import unittest
import pycodestyle

"""module that contains unittests for Base class"""

"""TestBase class that inherits from unittest.Testcase class"""


class TestBase(unittest.TestCase):

    def test_pep8(self):

        """checks pep8 style guide on every file"""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0, "Found code style error (and warnings).")


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
