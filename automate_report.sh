#!/bin/bash

# Navigate to the project directory
cd /workspaces/test

# Run your fetch_and_grep.sh script
./fetch_and_grep.sh

# Run your Python script to send the email
python3 send_email.py
