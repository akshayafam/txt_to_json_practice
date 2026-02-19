#!/bin/bash

# This is our automation bash script

echo "------------------------------------------"
echo "Starting Modernization Job:  $(date)"
echo "------------------------------------------"

echo "[STEP 1/3] Generating 100 legacy records..."
python3 generate_test_data.py

if [ -f "mainframe_data.txt" ]; then
    echo "[STEP 2/3] Success. Converting to JSON..."
    python3 batch_modernize.py
else
    echo "[ERROR] Step 1 failed! 'mainframe_data.txt' not found."
    exit 1
fi

if [ -f "modernized_data.json" ]; then
    echo "[STEP 3/3] Migration Complete!"
    echo "------------------------------------------"
    echo "Summary of files created:"
    ls -lh *.txt *.json
else
    echo "[ERROR] Step 2 failed! JSON file was not created."
    exit 1
fi