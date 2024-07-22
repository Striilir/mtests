#!/bin/bash

generate_mock_data() {
    cat <<EOL > mock_data.csv
Date,Niveau,Allonge,Assis,SessionID,formattedDate
1618937885,2,True,True,ed73e2a7-8f8a-493c-9388-c7cc4714b0ad,20/04/2021
1618937885,2,True,True,ed73e2a7-8f8a-493c-9388-c7cc4714b0ad,20/04/2021
1618937885,2,True,False,ed73e2a7-8f8a-493c-9388-c7cc4714b0ad,20/04/2021
1618937885,2,True,True,ed73e2a7-8f8a-493c-9388-c7cc4714b0ad,20/04/2021
1618937885,1,True,False,ed73e2a7-8f8a-493c-9388-c7cc4714b0ad,20/04/2021
1618941909,2,True,True,fd305c40-0331-4bc3-aac2626fdfa2,20/04/2021
1618941909,2,True,False,fd305c40-0331-4bc3-aac2626fdfa2,20/04/2021
1618990359,2,True,False,ed73e2a7-8f8a-493c-9388-c7cc4714b0ad,21/04/2021
1618996829,2,True,False,1e481168-243e-4e64-87d3-a2b5085a77a2,21/04/2021
1619017490,2,True,False,1e481168-243e-4e64-87d3-a2b5085a77a2,21/04/2021
EOL
}

generate_expected_output() {
    cat <<EOL > expected_output.csv
SessionID,Assis,Allonge,Niveau,formattedDate,Serie,Vie
ed73e2a7-8f8a-493c-9388-c7cc4714b0ad,True,True,2,20/04/2021,1,2
ed73e2a7-8f8a-493c-9388-c7cc4714b0ad,True,True,2,20/04/2021,1,2
ed73e2a7-8f8a-493c-9388-c7cc4714b0ad,False,True,2,20/04/2021,1,2
ed73e2a7-8f8a-493c-9388-c7cc4714b0ad,True,True,2,20/04/2021,1,2
ed73e2a7-8f8a-493c-9388-c7cc4714b0ad,False,True,1,20/04/2021,1,2
fd305c40-0331-4bc3-aac2626fdfa2,True,True,2,20/04/2021,2,2
fd305c40-0331-4bc3-aac2626fdfa2,False,True,2,20/04/2021,2,2
ed73e2a7-8f8a-493c-9388-c7cc4714b0ad,False,True,2,21/04/2021,2,2
1e481168-243e-4e64-87d3-a2b5085a77a2,False,True,2,21/04/2021,1,2
1e481168-243e-4e64-87d3-a2b5085a77a2,False,True,2,21/04/2021,1,2
EOL
}

# Test function
run_test() {
    description=$1
    command=$2
    expected_status=$3
    expected_file=$4

    echo "Running test: $description"
    echo "Command: $command"
    eval "$command"
    status=$?

    echo "Command status: $status"
    if [ $status -ne $expected_status ]; then
        echo "Test failed: Expected status $expected_status but got $status"
        return 1
    fi

    if [ ! -z "$expected_file" ] && [ ! -f "$expected_file" ]; then
        echo "Test failed: Expected file $expected_file not found"
        return 1
    fi

    if [ -n "$expected_file" ] && ! cmp -s "$expected_file" "output.csv"; then
        echo "Test failed: Expected file $expected_file does not match output"
        echo "Differences:"
        diff "$expected_file" "output.csv"
        return 1
    fi

    echo "Test passed: $description"
    return 0
}

# Setup
generate_mock_data
generate_expected_output

# Tests
run_test "Test script.sh with 2 lines" "./process_csv.sh -f mock_data.csv -o output.csv -n 2" 0 "expected_output.csv"
run_test "Test script.sh with no output file specified" "./process_csv.sh -f mock_data.csv -n 2" 0 "expected_output.csv"
run_test "Test script.sh without specifying input file" "./process_csv.sh -o output.csv -n 2" 1 ""
run_test "Test script.sh without specifying number of lines" "./process_csv.sh -f mock_data.csv -o output.csv" 0 "expected_output.csv"

# Cleanup
rm -f mock_data.csv
rm -f output.csv
rm -f expected_output.csv
rm -f temp_input.csv
