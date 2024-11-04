#!/usr/bin/env python3
"""unittest test script of utils.py"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test class for access_nested_map method"""
    @parameterized.expand([
        ('single_map', {"a": 1}, ("a",), 1),
        ('nested_map_depth_2', {"a": {"b": 2}}, ("a",), {"b": 2}),
        ('nested_map_2_path', {"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, name, nested_map, path, expected):
        """method to test access_nested_map method"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
