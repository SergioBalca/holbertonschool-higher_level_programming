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

        self.assertEqual(s_1.id, 8)
        self.assertEqual(s_2.area(), 4)
        self.assertEqual(s_3.display(), "\n\n\n ###\n ###\n ###\n")
