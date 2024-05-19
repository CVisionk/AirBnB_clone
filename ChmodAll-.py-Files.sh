#!/bin/bash

function check_style() {

  # Find all directories, including the current one and subdirectories
  find . -type d ! -path "*/.*" | while read -r dir; do
    # Run pycodestyle on all .py files in the current directory and all its subdirectories
    find "$dir" -type f -name "*.py" ! -name "__*" | while read -r file; do
      chmod +x "$file"
      # Print the checked file to stderr
      echo "Chmoded file $file" >&2
    done

    # Print the checked directory to stderr
    echo "chmoded on directory $dir" >&2
  done
}

# Run the check_style function with any additional arguments passed to the script
check_style "$@"

# Print completion message to stderr
echo "Finished chmodding .py files" >&2