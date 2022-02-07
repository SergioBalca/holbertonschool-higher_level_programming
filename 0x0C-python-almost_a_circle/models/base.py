#!/usr/bin/python3

"""module that has the Base class"""


class Base:

    """ Private class attribute """
    __nb_objects = 0

    def __init__(self, id=None):

        """ class constructor
            Args:
                id:     The id of the instance. if None
                        id will take the value of the
                        instance counter (__nb_objects)
        """
        if id is None:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
        else:
            self.id = id
