#!/usr/bin/python3
"""This module Defines a Rectangle"""

from models.base import Base


class Rectangle(Base):
    """
        It inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
            It initializes attributes of the object
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
            It returns width
        """
        return self.__width

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

    @property
    def height(self):
        """
        It returns height
        """
        return self.__height

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

    @property
    def x(self):
        """
        It returns x
        """
        return self.__x

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

    @property
    def y(self):
        """
        It returns y
        """
        return self.__y

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

    def area(self):
        """
        It calucalted the area
        """
        return self.__width * self.__height

    def display(self):
        """
        It displayss a rectangle using # symbol
        """
        if self.__height == 0 or self.__width == 0:
            print("")
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end="")
            if i < self.__height:
                print()

    def __str__(self):
        """
        It overrides the __str__ method
        """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - " \
            f"{self.__width}/{self.__height}"
