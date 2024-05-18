#!/usr/bin/env python3
import sys

def greet():
    while True:
        try:
            if not sys.stdin.isatty():  # Check if input is from a pipe
                name = sys.stdin.readline().strip()  # Read from standard input
            else:
                name = input("What's your name? ")  # Prompt user for input

            print("Hello, " + name + "!")
            choice = input("Do you want to greet another user? (yes/no): ").lower()
            if choice != "yes":
                break
        except EOFError:
            print("\nEOF reached. Exiting...")
            break

if __name__ == "__main__":
    greet()
