#!/usr/bin/python3
class Square:
    """
    Represents a square with a specific size.

    This class provides a way to create and manipulate square objects.

    Attributes:
    __size (int): The size of the square.

    """
    def __init__(self, size):
        """
        Initializes a new instance of the Square class.

        Args:
        size (int): The size of the square. Must be a positive integer.

        """
        self.__size = size
