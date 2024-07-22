#!/bin/bash

usage() {
    echo "Usage: $0 -f <input_file> -o <output_file> -n <num_lines>"
    exit 1
}

while getopts ":f:o:n:" opt; do
  case $opt in
    f) input_file="$OPTARG" ;;
    o) output_file="$OPTARG" ;;
    n) num_lines="$OPTARG" ;;
    *) usage ;;
  esac
done

if [ -z "$input_file" ]; then
    echo "Veuillez spécifier un fichier d'entrée"
    exit 1
fi

if [ -z "$output_file" ]; then
    output_file="./output.csv"
fi

if [ -z "$num_lines" ]; then
    num_lines=0
fi

# Extract the first num_lines from the input file
if [ "$num_lines" -gt 0 ]; then
    head -n $((num_lines + 1)) "$input_file" > temp_input.csv
    input_file="temp_input.csv"
fi

# Call the Python script to process the CSV
python3 process_csv.py -f "$input_file" -o "$output_file"
python_status=$?

# Clean up temporary file
if [ -f temp_input.csv ]; then
    rm temp_input.csv
fi

exit $python_status
