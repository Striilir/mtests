#!/bin/bash
echo "Running Python tests..."
python3 -m unittest discover -s . -p test_process_csv.py
echo "Python tests completed."
