#!/usr/bin/python3

from models.rectangle import Rectangle
from models.rectangle import Base
import unittest

"""module that contains unittest for Rectangle class"""

"""TestRectangle inherits from unittest.TestCase class"""


class TestRectangle(unittest.TestCase):
    def test_rectangle_id(self):

        """checks if Rectangle handles attribute id correctly"""

        r_1 = Base(20)
        r_2 = Rectangle(3, 2, 12, 0, 12)
        r_3 = Rectangle(2, 2, 5)
        r_4 = Rectangle(2, 2, 11, 0, -2)

        self.assertEqual(r_1.id, 20)
        self.assertEqual(r_2.id, 12)
        self.assertEqual(r_3.id, 7)
        self.assertEqual(r_4.id, -2)

    def test_attr_validation(self):

        """validates if arguments meet the requirements of each attribute"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "2")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r_2 = Rectangle(10, 2)
            r_2.y = float('Nan')
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 2, -3, 0)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r_4 = Rectangle(10, 2)
            r_4.y = -2

    def test_area(self):

        """Test for the area method"""

        r_1 = Rectangle(3, 2, 0, 0, 4)
        r_2 = Rectangle(2, 10, 0, 0, 15)
        r_3 = Rectangle(8, 7, 0, 0, 12)

        self.assertEqual(r_1.area(), 6)
        self.assertEqual(r_2.area(), 20)
        self.assertEqual(r_3.area(), 56)

    def test_display(self):

        """Test for display method"""

        r_1 = Rectangle(2, 2, 0, 0, 20)
        r_2 = Rectangle(3, 2, 0, 0, 21)
        r_3 = Rectangle(4, 6, 0, 0, 22)
        result_3 = "####\n####\n####\n"\
            "####\n####\n####\n"

        self.assertEqual(r_1.display(), "##\n##\n")
        self.assertEqual(r_2.display(), "###\n###\n")
        self.assertEqual(r_3.display(), result_3)

    def test_to_dictionary(self):

        """Test for to_dictionary method"""

        r_1 = Rectangle(1, 2, 3, 4, 5)
        r1_dictionary = r_1.to_dictionary()
        r_2 = Rectangle(**r1_dictionary)
        result = {'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        self.assertEqual(r1_dictionary, result)
        self.assertEqual(r_2.to_dictionary(), result)

    def test__str__(self):

        """Test for __str__ method"""

        r_1 = Rectangle(1, 2, 3, 4, 5)
        result = "[Rectangle] (5) 3/4 - 1/2"

        self.assertEqual(str(r_1), result)
