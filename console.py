#!/usr/bin/env python3
import sys

def doInput():
    try:
        while True:
            user_input = input("(hbnb) ")

            if user_input.lower() == 'quit':
                break
            elif user_input.lower() == 'help':
                if sys.stdin.isatty():
                    print(helper)
                else:
                    print("\n", helper)
    except EOFError:
        print("\nEOF reached. Exiting...")
        exit

helper = (
    "\nDocumented commands (type help <topic>):\n"
    "========================================\n"
    "EOF  help  quit\n"
)

doInput()
