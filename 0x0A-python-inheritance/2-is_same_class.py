#!/usr/bin/python3
"""
This module contains the function is_same_class
"""


def is_same_class(obj, a_class):
    """return true if the object is the exact class a_class, false otherwise"""
    return (type(obj) == a_class)
