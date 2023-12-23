#!/usr/bin/python3
""" test console """
from io import StringIO
import unittest
import console
import sys



class test_Console(unittest.TestCase):
    """doc doc"""

    def setUp(self):
        # Set up any necessary configurations or objects before each test
        pass

    def tearDown(self):
        # Clean up any resources after each test
        pass

    def test_create_valid_string(self):
        # Test creating an object with a valid string parameter
        result = self.run_command('create MyClass name="My_house"')
        self.assertIn("My_house", result)  # Check if the attribute is set correctly

    def test_create_invalid_attribute(self):
        # Test creating an object with an invalid attribute
        result = self.run_command('create MyClass invalid_attr=123')
        self.assertIn("Invalid attribute", result)

    def test_create_invalid_value_format(self):
        # Test creating an object with an invalid value format
        result = self.run_command('create MyClass age=abc')
        self.assertIn("Invalid value for attribute", result)

    def test_create_float_value(self):
        # Test creating an object with a valid float parameter
        result = self.run_command('create MyClass price=123.45')
        self.assertIn(123.45, result)  # Check if the attribute is set correctly

    def test_create_invalid_float_value(self):
        # Test creating an object with an invalid float parameter
        result = self.run_command('create MyClass price=abc.def')
        self.assertIn("Invalid value for attribute", result)

    def run_command(self, command):
        # Helper function to execute the command and capture the output
        captured_output = StringIO()
        sys.stdout = captured_output
        console.HBNBCommand().onecmd(command)
        sys.stdout = sys.__stdout__  # Reset redirect.
        return captured_output.getvalue()

    def test_documentation(self):
        """test documentation"""
        self.assertIsNotNone(console.__doc__)
    

if __name__ == '__main__':
    unittest.main()
