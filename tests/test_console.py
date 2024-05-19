#!/usr/bin/python3
"""
This module contains unit tests for the command-line interface
help command of the AirBnB clone project.
"""

import unittest
import subprocess


class TestHelpCommand(unittest.TestCase):
    """
    Test case for the 'help' command in the console
    of the AirBnB clone project.
    """

    def test_help_command(self):
        """
        Test that the 'help' command outputs the correct help information.
        """
        process = subprocess.Popen(['python3', 'console.py'],
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE, text=True)

        (output, _) = process.communicate(input='''help
quit
''')
        expected_output = \
            '''Documented commands (type help <topic>):
========================================
EOF  help  quit
'''

        self.assertIn(expected_output, output)


if __name__ == '__main__':
    unittest.main()
