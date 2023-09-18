#!/usr/bin/python3

from models import Base


class Rectangle(Base):
    """
    It inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @width.setter
    def set_width(self, value):
        """
        It sets width
        """
        self.__width = value

    @height.setter
    def set_height(self, value):
        """
        It sets height
        """
        self.__height = value

    @x.setter
    def set_x(self, value):
        """
        It sets x
        """
        self.__x = value

    @y.setter
    def set_y(self, value):
        """
        It sets y
        """
        self.__y = value

    @property
    def get_width(self):
        """
        It returns width
        """
        return self.__width

    @property
    def get_height(self):
        """
        It returns height
        """
        return self.__height

    @property
    def get_x(self):
        """
        It returns x
        """
        return self.__x

    @property
    def get_y(self):
        """
        It returns y
        """
        return self.__y
