#!/usr/bin/python3

"""
    Defines unittests for base.py
"""
import unittest
from models.Base import Base

class TestBase(unittest.TestCase):
    """ Unit testing """

    def test_instance_creation_with_id(self):
        """Test instance creation with a specific id."""
        obj = Base(42)
        self.assertEqual(obj.id, 42)

    def test_instance_creation_without_id(self):
        """Test instance creation without a specific id."""
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    if __name__ == '__main__':
        unittest.main()
