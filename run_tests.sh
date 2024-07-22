#!/bin/bash

# Function to run bash tests
run_bash_tests() {
    echo "Running Bash tests..."
    bash test_process_csv.sh
    if [ $? -eq 0 ]; then
        echo "Bash tests passed."
    else
        echo "Some Bash tests failed."
        return 1
    fi
}

# Function to run python tests
run_python_tests() {
    echo "Running Python tests..."
    python3 -m unittest discover -s . -p "test_process_csv.py"
    if [ $? -eq 0 ]; then
        echo "Python tests passed."
    else
        echo "Some Python tests failed."
        return 1
    fi
}

# Run bash tests
run_bash_tests
bash_test_result=$?
echo "Bash test result: $bash_test_result"

# Run python tests
run_python_tests
python_test_result=$?
echo "Python test result: $python_test_result"

# Summary of results
if [ $bash_test_result -eq 0 ] && [ $python_test_result -eq 0 ]; then
    echo "All tests passed successfully!"
    exit 0
else
    if [ $bash_test_result -ne 0 ]; then
        echo "Some Bash tests failed."
    fi
    if [ $python_test_result -ne 0 ]; then
        echo "Some Python tests failed."
    fi
    exit 1
fi
