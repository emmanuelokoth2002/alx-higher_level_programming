#!/usr/bin/python3

"""Unittests for max_integer([..])."""

import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))
    
    def test_single_item_list(self):
        self.assertEqual(max_integer([5]), 5)
    
    def test_sorted_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
    
    def test_unsorted_list(self):
        self.assertEqual(max_integer([3, 1, 5, 4, 2]), 5)
    
    def test_negative_numbers_list(self):
        self.assertEqual(max_integer([-5, -2, -7, -1, -9]), -1)
    
    def test_float_numbers_list(self):
        self.assertEqual(max_integer([1.5, 2.7, 3.2, 2.5]), 3.2)
    
    def test_mixed_numbers_list(self):
        self.assertEqual(max_integer([-5, 2, 3.5, -1.2, 4]), 4)
    
    def test_string_list(self):
        with self.assertRaises(TypeError):
            max_integer(["hello", "world", "!"])
    
    def test_mixed_types_list(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2, "three", 4, 5])

if __name__ == '__main__':
    unittest.main()
                    
