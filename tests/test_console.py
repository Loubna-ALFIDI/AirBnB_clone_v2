#!/usr/bin/python3
""" test console """
import unittest
import console


class test_Console(unittest.TestCase):
    """doc doc"""

    def test_documentation(self):
        """test documentation"""
        self.assertIsNotNone(console.__doc__)
