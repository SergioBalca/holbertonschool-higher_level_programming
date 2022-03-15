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

    def update(self, *args, **kwargs):

        """public method that assigns attributes by using args and kwargs"""

        attr_list = ["id", "size", "x", "y"]
        if len(args) != 0:
            for key, value in zip(attr_list, args):
                setattr(self, key, value)

        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):

        """ public method that returns the dictionray
            representation of a square class
        """
        key_list = ['id', 'size', 'x', 'y']
        value_list = []
        for key in key_list:
            value_list.append(getattr(self, key))
        return dict(zip(key_list, value_list))
