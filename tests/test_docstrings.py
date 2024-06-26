#!/usr/bin/python3
"""
This module contains a unittest test suite for checking the presence
of docstrings in Python files within a specified directory.
"""

import unittest
import ast
import os


class FileNavigator():
    """FIleNavigator class for finding python files within project folder"""

    def __init__(self, start_directory):
        """Sets start_directory"""
        self.start_directory = start_directory

    def find_python_files(self):
        """
        This function traverses the directory structure starting from the
        provided start_directory, searching for Python files (ending with .py).

        Returns:
            A list of full paths to all Python files found.
        """
        python_files = []
        for root, _, files in os.walk(self.start_directory):
            for file in files:
                if file.endswith('.py'):
                    path = os.path.join(root, file)
                    python_files.append(path)
        return python_files

    def find_python_files(self):
        """
        This function traverses the directory structure starting from the
        provided start_directory, searching for Python files (ending with .py).

        Returns:
            A list of full paths to all Python files found.
        """
        python_files = []
        for root, _, files in os.walk(self.start_directory):
            for file in files:
                if file.endswith('.py'):
                    path = os.path.join(root, file)
                    python_files.append(path)
        return python_files


def create_test(file_path):
    """
    Create a test method to check for docstrings in a specific file.

    Args:
        file_path (str): The path to the Python file to be tested.

    Returns:
        function: A test method that checks for the presence of docstrings.
    """
    def test(self):
        with open(file_path, 'r') as file:
            node = ast.parse(file.read(), filename=file_path)
            self.check_docstrings(node, file_path)
    return test


class TestDocstrings(unittest.TestCase):
    """
    Test case for checking the presence of docstrings in Python files.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the test suite by finding all Python files in
        the specified directory.
        """
        # You can specify the directory you want to start searching from here
        navigator = FileNavigator('.')
        cls.python_files = navigator.find_python_files()

    def check_docstrings(self, node, file_path):
        """
        Recursively check for docstrings in modules, classes, and functions.

        Args:
            node (ast.AST): The AST node representing the Python file.
            file_path (str): The path to the Python file being checked.
        """
        # Check module docstring
        if not ast.get_docstring(node):
            self.fail(f'Module in {file_path} is missing a docstring.')

        for item in node.body:
            if isinstance(item, ast.ClassDef):
                # Check class docstring
                if not ast.get_docstring(item):
                    self.fail(
                        'Class {} in {} is missing a docstring.'
                        .format(item.name, file_path))
                # Check methods in class
                for class_item in item.body:
                    if isinstance(class_item, ast.FunctionDef):
                        if not ast.get_docstring(class_item):
                            self.fail(
                                'Method {} in class {} in {} missing docstring'
                                .format(class_item, item.name, file_path))
            elif isinstance(item, ast.FunctionDef):
                # Check function docstring
                if not ast.get_docstring(item):
                    self.fail(
                        'Function {} in {} is missing a docstring.'
                        .format(item.name, file_path))


# Dynamically create test methods for each file
def add_dynamic_tests():
    """
    Dynamically create test methods for each Python file
    found by the FileNavigator.
    """
    navigator = FileNavigator('.')
    python_files = navigator.find_python_files()
    for file_path in python_files:
        test_method = create_test(file_path)
        test_path = file_path.replace("/", "_").replace(".", "_")
        test_name = f'test_docstring_{test_path}'
        setattr(TestDocstrings, test_name, test_method)


# Ensure dynamic tests are added before running unittest
add_dynamic_tests()

if __name__ == '__main__':
    unittest.main()
