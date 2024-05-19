#!/usr/bin/python3
"""
Tester temp file.
"""
import os


def list_all_files(directory):
    """
    This function lists all files from the specified
    directory and its subdirectories.

    Args:
        directory: The path to the directory to search.
    """
    for root, _, files in os.walk(directory):
        for file in files:
            # Construct full path
            full_path = os.path.join(root, file)
            # print(full_path)


# Example usage (replace "path/to/your/directory" with your actual path)
list_all_files("..")
