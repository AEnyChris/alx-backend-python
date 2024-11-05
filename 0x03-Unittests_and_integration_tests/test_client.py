#!/usr/bin/env python3
"""Test script for client.py"""
import unittest
from unittest.mock import patch
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """Test class for testting GithubOrgClient class and methods"""
    @parameterized.expand([
        ('google'),
        ('abc')
        ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_org):
        """test method for .org method"""
        inst = GithubOrgClient(org_name)
        result = inst.org

        mock_org.assert_called_once_with(inst.ORG_URL.format(org=org_name))
