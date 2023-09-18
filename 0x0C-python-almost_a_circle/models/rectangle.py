#!/usr/bin/python3
"""
Define a Rectangle
"""

from models.base import Base


class Rectangle(Base):
    """
    It inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        It nitializes attributes of the object
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @width.setter
    def width(self, value):
        """
        It sets width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        It sets height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """
        It sets x
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """
        It sets y
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @property
    def width(self):
        """
        It returns width
        """
        return self.__width

    @property
    def height(self):
        """
        It returns height
        """
        return self.__height

    @property
    def x(self):
        """
        It returns x
        """
        return self.__x

    @property
    def y(self):
        """
        It returns y
        """
        return self.__y

    def area(self):
        """
        It calucalted the area
        """
        return self.__width * self.__height

    def display(self):
        """
        It returns a rectangle using # symbol
        """
        if self.__height == 0 or self.__width == 0:
            return ""
        rectangle = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle += "#"
            if i < self.__height - 1:
                rectangle += "\n"
        return rectangle
