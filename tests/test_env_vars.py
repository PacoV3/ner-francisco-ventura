# import pytest
import unittest
import sys 
import os


# import the function from your file
directory_path = os.path.abspath(os.path.join('.'))
if directory_path not in sys.path:
    sys.path.append(directory_path)

print(sys.path)

from src.functions.env_vars import get_env_variable, get_env_path


class env_vars_test(unittest.TestCase):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setUp()

    # Check if get_env_variable returns a String
    def test_get_env_variable_return_string(self):
        expect_type = type('')
        f_result = get_env_variable('ENV_TEST')
        f_result_type = type(f_result)
        self.assertEqual(expect_type, f_result_type)

    # Check if get_env_variable returns the correct value
    def test_get_env_variable_return_value(self):
        expect_value = 'Hola Mundo!'
        f_result = get_env_variable('ENV_TEST')
        self.assertEqual(expect_value, f_result)

if __name__ == '__main__':
    get_env_variable('ENV_TEST')
    get_env_path()
