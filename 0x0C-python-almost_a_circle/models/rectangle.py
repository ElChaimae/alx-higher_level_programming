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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def set_height(self, value):
        """
        It sets height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def set_x(self, value):
        """
        It sets x
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def set_y(self, value):
        """
        It sets y
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
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
