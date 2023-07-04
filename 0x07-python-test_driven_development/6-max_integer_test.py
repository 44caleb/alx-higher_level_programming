#!/usr/bin/python3
"""unit test for "max_integer" function"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unit test for max_integer"""

    def testBasic(self):
        my_list = [1, 3, 2, 4]
        self.assertEqual(max_integer(my_list), 4)

    def testOneElement(self):
        """test single element"""
        my_list = [1]
        self.assertEqual(max_integer(my_list), 1)

    def testEmptyList(self):
        """tests empty list"""
        my_list = []
        self.assertEqual(max_integer(my_list), None)

    def testRandom(self):
        """test for different types"""
        my_list = [1, 4, 'A']
        self.assertRaises(TypeError, max_integer, my_list)

    def testFloats(self):
        """Test a list of floats."""
        floats = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 15.2)

    def testPassDict(self):
        my_list = {0: 'a', 1: 'z', 2: 'c'}
        self.assertEqual(max_integer(my_list), 'z')


if __name__ == '__main__':
    unittest.main()
