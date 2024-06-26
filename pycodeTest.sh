#!/bin/bash

function check_style() {
  # Ensure pycodestyle is installed
  if ! command -v pycodestyle &> /dev/null; then
    echo "pycodestyle is not installed. Please install it first." >&2
    exit 1
  fi

  # Find all directories, including the current one and subdirectories
  find . -type d ! -path "*/.*" | while read -r dir; do
    # Run pycodestyle on all .py files in the current directory and all its subdirectories
    find "$dir" -type f -name "*.py" ! -name "__*" | while read -r file; do
      pycodestyle "$file"
      # Print the checked file to stderr
      echo "Checked file $file" >&2
    done

    # Print the checked directory to stderr
    echo "Checked directory $dir" >&2
  done
}

# Run the check_style function with any additional arguments passed to the script
check_style "$@"

# Print completion message to stderr
echo "Finished checking code style!" >&2