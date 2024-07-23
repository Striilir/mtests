import unittest
from process_csv import read_csv, write_csv, clean_input_data, streak_user
import os

class TestProcessCSV(unittest.TestCase):

    def setUp(self):
        # Setup code with sample data
        self.input_file = 'mock_data.csv'
        self.output_file = 'output.csv'
        self.cleaned_data = [
            {"Date": "1618937885", "Niveau": "2", "Allonge": "True", "Assis": "True", "SessionID": "ed73e2a7-8f8a-493c-9388-c7cc4714b0ad", "formattedDate": "20/04/2021"},
            {"Date": "1618937885", "Niveau": "2", "Allonge": "True", "Assis": "True", "SessionID": "ed73e2a7-8f8a-493c-9388-c7cc4714b0ad", "formattedDate": "20/04/2021"},
            {"Date": "1618937885", "Niveau": "2", "Allonge": "False", "Assis": "True", "SessionID": "ed73e2a7-8f8a-493c-9388-c7cc4714b0ad", "formattedDate": "20/04/2021"},
            {"Date": "1618937885", "Niveau": "2", "Allonge": "True", "Assis": "True", "SessionID": "ed73e2a7-8f8a-493c-9388-c7cc4714b0ad", "formattedDate": "20/04/2021"},
            {"Date": "1618937885", "Niveau": "1", "Allonge": "True", "Assis": "False", "SessionID": "ed73e2a7-8f8a-493c-9388-c7cc4714b0ad", "formattedDate": "20/04/2021"}
        ]
        self.mock_data_content = """Date,Niveau,Allonge,Assis,SessionID,formattedDate
1618937885,2,True,True,ed73e2a7-8f8a-493c-9388-c7cc4714b0ad,20/04/2021
1618937885,2,True,True,ed73e2a7-8f8a-493c-9388-c7cc4714b0ad,20/04/2021
1618937885,2,True,False,ed73e2a7-8f8a-493c-9388-c7cc4714b0ad,20/04/2021
1618937885,2,True,True,ed73e2a7-8f8a-493c-9388-c7cc4714b0ad,20/04/2021
1618937885,1,True,False,ed73e2a7-8f8a-493c-9388-c7cc4714b0ad,20/04/2021
"""
        with open(self.input_file, 'w') as f:
            f.write(self.mock_data_content)

    def tearDown(self):
        if os.path.exists(self.input_file):
            os.remove(self.input_file)
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_read_csv(self):
        data = read_csv(self.input_file)
        self.assertEqual(len(data), 5)  # Replace with the expected number of rows in your CSV

    def test_write_csv(self):
        write_csv(self.cleaned_data, self.output_file)
        with open(self.output_file, 'r') as f:
            lines = f.readlines()
            self.assertEqual(len(lines), 6)  # One header line + five data lines

    def test_clean_input_data(self):
        cleaned_data = clean_input_data(self.cleaned_data)
        self.assertEqual(cleaned_data[0]["formattedDate"], "20/04/2021")

    def test_streak_user(self):
        streaked_data = streak_user(self.cleaned_data)
        expected_streak_data = [
            {"Date": "1618937885", "Niveau": "2", "Allonge": "True", "Assis": "True", "SessionID": "ed73e2a7-8f8a-493c-9388-c7cc4714b0ad", "formattedDate": "20/04/2021", "Serie": "1", "Vie": "2"},
            {"Date": "1618937885", "Niveau": "2", "Allonge": "True", "Assis": "True", "SessionID": "ed73e2a7-8f8a-493c-9388-c7cc4714b0ad", "formattedDate": "20/04/2021", "Serie": "1", "Vie": "2"},
            {"Date": "1618937885", "Niveau": "2", "Allonge": "False", "Assis": "True", "SessionID": "ed73e2a7-8f8a-493c-9388-c7cc4714b0ad", "formattedDate": "20/04/2021", "Serie": "1", "Vie": "2"},
            {"Date": "1618937885", "Niveau": "2", "Allonge": "True", "Assis": "True", "SessionID": "ed73e2a7-8f8a-493c-9388-c7cc4714b0ad", "formattedDate": "20/04/2021", "Serie": "1", "Vie": "2"},
            {"Date": "1618937885", "Niveau": "1", "Allonge": "True", "Assis": "False", "SessionID": "ed73e2a7-8f8a-493c-9388-c7cc4714b0ad", "formattedDate": "20/04/2021", "Serie": "1", "Vie": "2"}
        ]
        self.assertEqual(streaked_data, expected_streak_data)

if __name__ == "__main__":
    unittest.main()
