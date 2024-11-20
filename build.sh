#!/bin/bash

# Install required packages
pip install pyinstaller

# Create the executable
pyinstaller --onefile --windowed --name FileReplacer file_replacer.py

echo "Executable creation completed!"