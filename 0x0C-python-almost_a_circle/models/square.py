#!/usr/bin/python3

"""module with the Square class"""

from models.rectangle import Rectangle

"""Square class inherits from Rectangle class"""


class Square(Rectangle):

    """ Square class that inherits from Rectangle class
        Args:
            size: size of the square
    """
    def __init__(self, size, x=0, y=0, id=None):

        """constructor for Square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):

        """__str__ method is used to print a square instance"""
        return "[{}] ({}) {}/{} - {}".format(
            __class__.__name__, self.id, self.x,
            self.y, self.width
            )

    @property
    def size(self):
        """property to retrive size value"""
        return self.width

    @size.setter
    def size(self, value):
        """ the Rectangle arguments validations are used to set
            size value
        """
        self.width = value
        self.height = value
