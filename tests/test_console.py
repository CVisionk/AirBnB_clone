#!/usr/bin/env python3
import unittest
import subprocess

class TestHelpCommand(unittest.TestCase):
    def test_help_command(self):
        process = subprocess.Popen(
                ['python3', 'console.py'],
                  stdin=subprocess.PIPE,
                  stdout=subprocess.PIPE,
                  stderr=subprocess.PIPE,
                  text=True)

        output, _ = process.communicate(input='help\nquit\n')
        expected_output = (
                "Documented commands (type help <topic>):\n"
                "========================================\n"
                "EOF  help  quit\n"
        )

        self.assertIn(expected_output, output)

if __name__ == '__main__':
    unittest.main()
