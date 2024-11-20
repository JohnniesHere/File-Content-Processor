#!/bin/bash

# Install required packages
pip install pyinstaller

# Create the executable
pyinstaller --onefile --windowed --name FileContentProcessor file_replacer.py

echo "Executable creation completed!"