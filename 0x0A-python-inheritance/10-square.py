#!/usr/bin/python3
""" Module containing the Rectangle class """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class representing a rectangle """

    def __init__(self, width, height):
        """ Initialize a rectangle instance """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Calculate the area of the rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ Return a string representation of the rectangle """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """ Class representing a square """

    def __init__(self, size):
        """ Initialize a square instance """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """ Return a string representation of the square """
        return "[Square] {}/{}".format(self.__size, self.__size)

