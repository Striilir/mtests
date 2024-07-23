#!/bin/bash

echo "Running Bash tests..."

# Create mock_data.csv before running the tests
cat <<EOF > mock_data.csv
"Date","Niveau","Allonge","Assis","SessionID","formattedDate"
"1618937885","2","True","True","ed73e2a7-8f8a-493c-9388-c7cc4714b0ad","20/04/2021"
"1618937885","2","True","True","ed73e2a7-8f8a-493c-9388-c7cc4714b0ad","20/04/2021"
"1618937885","2","True","False","ed73e2a7-8f8a-493c-9388-c7cc4714b0ad","20/04/2021"
"1618937885","2","True","True","ed73e2a7-8f8a-493c-9388-c7cc4714b0ad","20/04/2021"
"1618937885","1","True","False","ed73e2a7-8f8a-493c-9388-c7cc4714b0ad","20/04/2021"
EOF

# Create expected_output.csv before running the tests
cat <<EOF > expected_output.csv
"Date","Niveau","Allonge","Assis","SessionID","formattedDate","Serie","Vie"
"1618937885","2","True","True","ed73e2a7-8f8a-493c-9388-c7cc4714b0ad","20/04/2021","1","2"
"1618937885","2","True","True","ed73e2a7-8f8a-493c-9388-c7cc4714b0ad","20/04/2021","1","2"
"1618937885","2","True","False","ed73e2a7-8f8a-493c-9388-c7cc4714b0ad","20/04/2021","1","2"
"1618937885","2","True","True","ed73e2a7-8f8a-493c-9388-c7cc4714b0ad","20/04/2021","1","2"
"1618937885","1","True","False","ed73e2a7-8f8a-493c-9388-c7cc4714b0ad","20/04/2021","1","2"
EOF

echo "Running test: Test script.sh with 2 lines"
OUTPUT=$(./process_csv.sh -f mock_data.csv -o output.csv -n 2)
STATUS=$?
if [ $STATUS -ne 0 ]; then
    echo "Test failed: Script exited with status $STATUS"
else
    diff -u <(tail -n +2 output.csv) <(tail -n +2 expected_output.csv)
    if [ $? -ne 0 ]; then
        echo "Test failed: Expected file expected_output.csv does not match output"
    else
        echo "Test passed"
    fi
fi

echo "Running test: Test script.sh with no output file specified"
OUTPUT=$(./process_csv.sh -f mock_data.csv -n 2)
STATUS=$?
if [ $STATUS -ne 0 ]; then
    echo "Test failed: Script exited with status $STATUS"
else
    diff -u <(tail -n +2 output.csv) <(tail -n +2 expected_output.csv)
    if [ $? -ne 0 ]; then
        echo "Test failed: Expected file expected_output.csv does not match output"
    else
        echo "Test passed"
    fi
fi

echo "Running test: Test script.sh without specifying input file"
OUTPUT=$(./process_csv.sh -o output.csv -n 2 2>&1)
STATUS=$?
if [ $STATUS -eq 0 ]; then
    echo "Test failed: Script should have exited with a non-zero status"
else
    if [[ $OUTPUT == *"Veuillez spécifier un fichier d'entrée"* ]]; then
        echo "Test passed"
    else
        echo "Test failed: Expected error message not found"
    fi
fi

echo "Running test: Test script.sh without specifying number of lines"
OUTPUT=$(./process_csv.sh -f mock_data.csv -o output.csv)
STATUS=$?
if [ $STATUS -ne 0 ]; then
    echo "Test failed: Script exited with status $STATUS"
else
    diff -u <(tail -n +2 output.csv) <(tail -n +2 expected_output.csv)
    if [ $? -ne 0 ]; then
        echo "Test failed: Expected file expected_output.csv does not match output"
    else
        echo "Test passed"
    fi
fi

echo "Bash tests passed."
echo "Bash test result: 0"

echo "Running Python tests..."
python3 -m unittest discover -s . -p test_process_csv.py
echo "Python tests completed."
