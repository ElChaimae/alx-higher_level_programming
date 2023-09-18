#!/usr/bin/python3
"""
Defines a Base Class
"""


class Base:
    """ This class is the “base” of all other classes in this project """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Class Constructor
        Args:
            id (int): instance identifier
        """
        if id is not None:
            self.id = id
        else:
            self.__nb_objects += 1
