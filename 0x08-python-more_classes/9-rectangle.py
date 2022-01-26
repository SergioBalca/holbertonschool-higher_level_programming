#!/usr/bin/python3

"""Class Rectangle definition"""


class Rectangle:

    """Model of a Rectangle"""

    """class attribute that increments during each new instance instantiation
    and decrements during each instance deletion
    """

    number_of_instances = 0

    """class attribute that defines a character to print the rectangle"""

    print_symbol = "#"

    """static method than compares two rectangles
    and retun the one with the biggest area
    """

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):

        """Return the rectangle with the biggest area.
        Arguments:
                 rect_1: an instance of class Rectangle
                 rect_2: an instance of class Rectangle
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    def __init__(self, width=0, height=0):

        """__init__ method for the Rectangle class
        Arguments:
        private instance width: integer that defines the width of rectangle
        private instance height: integer that defines the height of rectangle
        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    """property to retrieve width of the rectangle"""

    @property
    def width(self):
        return self.__width

    """property to set the value of width of the rectangle"""

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    """property to retreive height of the rectangle"""

    @property
    def height(self):
        return self.__height

    """property to set the value of height of rectangle"""

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    """public instance method to return rectangle area"""

    def area(self):
        return self.__width * self.__height

    """public instance method to return rectangle perimeter"""

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width + 2 * self.__height)

    """str method to print a given rectangle"""

    def __str__(self):
        result = ""
        if self.__width == 0 or self.__height == 0:
            return result
        else:
            for element in range(self.__height):
                result += str(self.print_symbol) * self.__width
                if element != self.__height - 1:
                    result += "\n"
        return result

    """ repr method that allows to recreate a new instance by using eval()"""

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    """ __del__ method to print a message when an instance is destroyed"""

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    """class method that returns a new Rectangle instance with width == height"""

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
