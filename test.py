#!/usr/bin/env python3
import sys
import os

helper = (
    "Documented commands (type help <topic>):\n"
    "========================================\n"
    "EOF  help  quit"
)

def handle_input(user_input):
    if user_input.lower() == 'quit':
        return False
    elif user_input.lower() == 'help':
        print(helper)
    else:
        print(f"You entered: {user_input}")
    return True

def main():
    is_interactive = os.isatty(sys.stdin.fileno())

    # Handle piped input if any
    if not is_interactive:
        for line in sys.stdin:
            if not handle_input(line.strip()):
                return

    # Switch to interactive mode
    try:
        while True:
            try:
                user_input = input("(hbnb) ")
                if not handle_input(user_input):
                    break
            except EOFError:
                if is_interactive:
                    print("\nEOF received, exiting.")
                    break
                else:
                    continue
    except KeyboardInterrupt:
        print("\nKeyboard interrupt received, exiting.")

if __name__ == "__main__":
    main()
