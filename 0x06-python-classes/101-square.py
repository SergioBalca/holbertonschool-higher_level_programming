#!/usr/bin/python3

"""Class Square defined"""


class Square:

    """Constructor with size and position
    of a square as arguments
    """

    def __init__(self, size=0, position=(0, 0)):

        self.size = size
        self.position = position

    """property to retrieve the size of the square"""

    @property
    def size(self):
        return self.__size

    """setter to set the value of square size"""

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """public instance method that returns the areas of
    a given square
    """

    def area(self):
        return self.__size ** 2

    """public instance method that prints in stdout the square
    with the character #
    """

    def my_print(self):
        if self.__size == 0:
            print()

        else:
            for y in range(self.__position[1]):
                print()
            for x in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

    """property to retrieve the value of square position"""

    @property
    def position(self):
        return self.__position

    """setter to set the value of square position"""

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    """__str__ method is used to print a square instance, instead of my_print method"""

    def __str__(self):
        result = ""
        if self.__size == 0:
            return result

        else:
            for y in range(self.__position[1]):
                result += "\n"
            for x in range(self.__size):
                result += " " * self.__position[0]
                result += "#" * self.__size
                if x != self.__size - 1:
                    result += "\n"
        return result
