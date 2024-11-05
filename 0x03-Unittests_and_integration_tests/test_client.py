#!/usr/bin/env python3
"""Test script for client.py"""
import unittest
from unittest.mock import patch
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """Test class for testting GithubOrgClient class and methods"""
    @parameterized.expand([
        ('google'),
        ('abc')
        ])
    @patch('client.get_json')
    def test_org(self, org, mock_org):
        """test method for .org method"""
        inst = GithubOrgClient(org)
        result = inst.org

        mock_org.assert_called_once_with(inst.ORG_URL.format(org=org))

    def test_public_repos_url(self):
        """method to test _public_repos_url method"""
        with patch.object(GithubOrgClient, 'org', new=TEST_PAYLOAD[0][0]):
            test_inst = GithubOrgClient('google')
            result = test_inst._public_repos_url

            self.assertEqual(result, TEST_PAYLOAD[0][0]['repos_url'])
