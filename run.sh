#!/bin/bash

# Check if folder "venv" exists
FOLDER=venv
if [ -d "$FOLDER" ]; then
	# Activate virtual environment
    source ./venv/bin/activate
else 
    # Create virtual environment
    python3 -m venv venv
    # Activate virtual environment
    source ./venv/bin/activate
    # Update pip
    pip install --upgrade pip
    pip install -r requirements.txt
fi

# Run main.py
python3 main.py
