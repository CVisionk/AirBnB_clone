#!/usr/bin/env python3
import sys
import cmd

class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        quits when prompted
        """
        return True
    def do_EOF(self, arg):
        """
        EOF signal to exit the program.
        """
        print("")
        return True
if __name__ == '__main__':
    HBNBCommand().cmdloop()