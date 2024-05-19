#!/usr/bin/python3
"""
Defines the HBNB console.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    A command-line interface for interacting
    with an Airbnb application console.

    Args:
        cmd (cmd.Cmd, optional): This is the base class from the `cmd` module
                                 that provides functionalities for building
                                 command-line interfaces.
                                 Inheriting from `cmd.Cmd` allows this class
                                 to define
                                 commands and handle user input for the
                                 Airbnb console.
                                 Defaults to None (automatically inherited).
    """
    prompt = "(hbnb) "

    def do_quit(self, args):
        """
        quits when prompted
        """
        exit()

    def do_EOF(self):
        """
        EOF signal to exit the program.
        """
        exit()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
