#!/usr/bin/env python3
"""unittest test script of utils.py"""
import unittest
from parameterized import parameterized
from utils import memoize, get_json, access_nested_map
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """Test class for access_nested_map method"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map, path, expected):
        """method to test access_nested_map method"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
        ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """method to test exception on access_nested_map method"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test class for get_json method"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    def test_get_json(self, test_url, test_payload):
        """tests get_json function with a mock url call"""
        with patch('utils.requests.get') as mock_get:
            mock_get.return_value.json.return_value = test_payload
            result = get_json(test_url)
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(test_payload, result)


class TestMemoize(unittest.TestCase):
    """Test class for memoize decorator"""
    def test_memoize(self):
        """method to test memoize using inner defined class TestClass"""
        class TestClass:
            """a Test class created for test only"""
            def a_method(self):
                """a_method is to be called to test memoize"""
                return 42

            @memoize
            def a_property(self):
                """calls the a_method for a test"""
                return self.a_method()

        with patch.object(TestClass,
                          'a_method',
                          return_value=42) as mock_a_method:
            inst_test = TestClass()
            result1 = inst_test.a_property
            result2 = inst_test.a_property

            mock_a_method.assert_called_once()
            self.assertEqual(result1, 42)
            self.assertEqual(result1, result2)
