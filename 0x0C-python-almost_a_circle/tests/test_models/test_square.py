#!/usr/bin/python3

from models.rectangle import Rectangle
from models.square import Square
import unittest

"""module that contains unittest for Square class"""

"""TestSquare inherits from unittest.TestCase"""


class TestSquare(unittest.TestCase):

    def test_square(self):

        """ checks if Square handles attributes and methods
            from Rectangle and Base class properly
        """

        s_1 = Square(5)
        s_2 = Square(2, 2)
        s_3 = Square(3, 1, 3)
        s_4 = Square(3, 1, 3, 15)
        s_4.update(1, 2, 3, 4)
        s_5 = Square(1, 2, 3, 4)
        s_5.update(size=7, id=89, y=1, x=1)

        self.assertEqual(s_1.id, 10)
        self.assertEqual(s_2.area(), 4)
        self.assertEqual(s_3.display(), "\n\n\n ###\n ###\n ###\n")
        self.assertEqual(s_4.x, 3)
        self.assertEqual(s_5.id, 89)
        self.assertEqual(s_5.x, 1)
        self.assertEqual(s_5.size, 7)

    def test_attr_validation(self):

        """checks if arguments meet attributes requirements"""

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("4")
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -2, 0, 2)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 0, float('Nan'), 3)

    def test_to_dictionary(self):

        "Test for to_dictionary method"

        s_1 = Square(2, 3, 4, 10)
        s1_dictionary = s_1.to_dictionary()
        result = {'id': 10, 'size': 2, 'x': 3, 'y': 4}
        s_2 = Square(**s1_dictionary)

        self.assertEqual(s1_dictionary, result)
        self.assertEqual(s_2.to_dictionary(), result)

    def test__str__(self):

        """Test for __str__ method"""

        s_1 = Square(1, 2, 3, 4)
        result = "[Square] (4) 2/3 - 1"

        self.assertEqual(str(s_1), result)
