import unittest
from process_csv import read_csv, write_csv, clean_input_data, streak_user
import os
import csv

class TestProcessCSV(unittest.TestCase):

    def setUp(self):
        self.input_data = [
            {'Date': '1618937885', 'Niveau': '2', 'Allonge': 'True', 'Assis': 'True', 'SessionID': 'ed73e2a7-8f8a-493c-9388-c7cc4714b0ad'},
            {'Date': '1618937885', 'Niveau': '2', 'Allonge': 'True', 'Assis': 'True', 'SessionID': 'ed73e2a7-8f8a-493c-9388-c7cc4714b0ad'},
            {'Date': '1618937885', 'Niveau': '2', 'Allonge': 'True', 'Assis': 'False', 'SessionID': 'ed73e2a7-8f8a-493c-9388-c7cc4714b0ad'},
            {'Date': '1618937885', 'Niveau': '2', 'Allonge': 'True', 'Assis': 'True', 'SessionID': 'ed73e2a7-8f8a-493c-9388-c7cc4714b0ad'},
            {'Date': '1618937885', 'Niveau': '1', 'Allonge': 'True', 'Assis': 'False', 'SessionID': 'ed73e2a7-8f8a-493c-9388-c7cc4714b0ad'},
            {'Date': '1618941909', 'Niveau': '2', 'Allonge': 'True', 'Assis': 'True', 'SessionID': 'fd305c40-0331-4bc3-aac2626fdfa2'},
            {'Date': '1618941909', 'Niveau': '2', 'Allonge': 'True', 'Assis': 'False', 'SessionID': 'fd305c40-0331-4bc3-aac2626fdfa2'},
            {'Date': '1618990359', 'Niveau': '2', 'Allonge': 'True', 'Assis': 'False', 'SessionID': 'ed73e2a7-8f8a-493c-9388-c7cc4714b0ad'},
            {'Date': '1618996829', 'Niveau': '2', 'Allonge': 'True', 'Assis': 'False', 'SessionID': '1e481168-243e-4e64-87d3-a2b5085a77a2'},
            {'Date': '1619017490', 'Niveau': '2', 'Allonge': 'True', 'Assis': 'False', 'SessionID': '1e481168-243e-4e64-87d3-a2b5085a77a2'}
        ]
        self.expected_cleaned_data = [
            {'Date': '1618937885', 'Niveau': '2', 'Allonge': 'True', 'Assis': 'True', 'SessionID': 'ed73e2a7-8f8a-493c-9388-c7cc4714b0ad', 'formattedDate': '20/04/2021'},
            {'Date': '1618937885', 'Niveau': '2', 'Allonge': 'True', 'Assis': 'True', 'SessionID': 'ed73e2a7-8f8a-493c-9388-c7cc4714b0ad', 'formattedDate': '20/04/2021'},
            {'Date': '1618937885', 'Niveau': '2', 'Allonge': 'True', 'Assis': 'False', 'SessionID': 'ed73e2a7-8f8a-493c-9388-c7cc4714b0ad', 'formattedDate': '20/04/2021'},
            {'Date': '1618937885', 'Niveau': '2', 'Allonge': 'True', 'Assis': 'True', 'SessionID': 'ed73e2a7-8f8a-493c-9388-c7cc4714b0ad', 'formattedDate': '20/04/2021'},
            {'Date': '1618937885', 'Niveau': '1', 'Allonge': 'True', 'Assis': 'False', 'SessionID': 'ed73e2a7-8f8a-493c-9388-c7cc4714b0ad', 'formattedDate': '20/04/2021'},
            {'Date': '1618941909', 'Niveau': '2', 'Allonge': 'True', 'Assis': 'True', 'SessionID': 'fd305c40-0331-4bc3-aac2626fdfa2', 'formattedDate': '20/04/2021'},
            {'Date': '1618941909', 'Niveau': '2', 'Allonge': 'True', 'Assis': 'False', 'SessionID': 'fd305c40-0331-4bc3-aac2626fdfa2', 'formattedDate': '20/04/2021'},
            {'Date': '1618990359', 'Niveau': '2', 'Allonge': 'True', 'Assis': 'False', 'SessionID': 'ed73e2a7-8f8a-493c-9388-c7cc4714b0ad', 'formattedDate': '21/04/2021'},
            {'Date': '1618996829', 'Niveau': '2', 'Allonge': 'True', 'Assis': 'False', 'SessionID': '1e481168-243e-4e64-87d3-a2b5085a77a2', 'formattedDate': '21/04/2021'},
            {'Date': '1619017490', 'Niveau': '2', 'Allonge': 'True', 'Assis': 'False', 'SessionID': '1e481168-243e-4e64-87d3-a2b5085a77a2', 'formattedDate': '21/04/2021'}
        ]
        self.cleaned_data = clean_input_data(self.input_data)
        self.output_file = 'test_output.csv'

    def tearDown(self):
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_read_csv(self):
        test_file = 'test_input.csv'
        with open(test_file, mode='w', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=self.input_data[0].keys(), quoting=csv.QUOTE_ALL)
            writer.writeheader()
            for row in self.input_data:
                writer.writerow(row)

        data = read_csv(test_file)
        self.assertEqual(len(data), 10)
        os.remove(test_file)

    def test_write_csv(self):
        streaked_data = streak_user(self.cleaned_data)
        write_csv(streaked_data, self.output_file)
        self.assertTrue(os.path.exists(self.output_file))

        # Vérifier que les données sont écrites correctement avec des guillemets
        with open(self.output_file, mode='r') as infile:
            reader = csv.DictReader(infile)
            rows = [row for row in reader]
            self.assertEqual(rows[0]['SessionID'], 'ed73e2a7-8f8a-493c-9388-c7cc4714b0ad')
            self.assertEqual(rows[0]['Serie'], '1')
            self.assertEqual(rows[0]['Vie'], '2')

    def test_clean_input_data(self):
        self.assertEqual(self.cleaned_data, self.expected_cleaned_data)

    def test_streak_user(self):
        streaked_data = streak_user(self.cleaned_data)
        expected_streak_data = [
            {'Date': '1618937885', 'Niveau': '2', 'Allonge': 'True', 'Assis': 'True', 'SessionID': 'ed73e2a7-8f8a-493c-9388-c7cc4714b0ad', 'formattedDate': '20/04/2021', 'Serie': '1', 'Vie': '2'},
            {'Date': '1618937885', 'Niveau': '2', 'Allonge': 'True', 'Assis': 'True', 'SessionID': 'ed73e2a7-8f8a-493c-9388-c7cc4714b0ad', 'formattedDate': '20/04/2021', 'Serie': '1', 'Vie': '2'},
            {'Date': '1618937885', 'Niveau': '2', 'Allonge': 'True', 'Assis': 'False', 'SessionID': 'ed73e2a7-8f8a-493c-9388-c7cc4714b0ad', 'formattedDate': '20/04/2021', 'Serie': '1', 'Vie': '2'},
            {'Date': '1618937885', 'Niveau': '2', 'Allonge': 'True', 'Assis': 'True', 'SessionID': 'ed73e2a7-8f8a-493c-9388-c7cc4714b0ad', 'formattedDate': '20/04/2021', 'Serie': '1', 'Vie': '2'},
            {'Date': '1618937885', 'Niveau': '1', 'Allonge': 'True', 'Assis': 'False', 'SessionID': 'ed73e2a7-8f8a-493c-9388-c7cc4714b0ad', 'formattedDate': '20/04/2021', 'Serie': '1', 'Vie': '2'},
            {'Date': '1618941909', 'Niveau': '2', 'Allonge': 'True', 'Assis': 'True', 'SessionID': 'fd305c40-0331-4bc3-aac2626fdfa2', 'formattedDate': '20/04/2021', 'Serie': '2', 'Vie': '2'},
            {'Date': '1618941909', 'Niveau': '2', 'Allonge': 'True', 'Assis': 'False', 'SessionID': 'fd305c40-0331-4bc3-aac2626fdfa2', 'formattedDate': '20/04/2021', 'Serie': '2', 'Vie': '2'},
            {'Date': '1618990359', 'Niveau': '2', 'Allonge': 'True', 'Assis': 'False', 'SessionID': 'ed73e2a7-8f8a-493c-9388-c7cc4714b0ad', 'formattedDate': '21/04/2021', 'Serie': '2', 'Vie': '2'},
            {'Date': '1618996829', 'Niveau': '2', 'Allonge': 'True', 'Assis': 'False', 'SessionID': '1e481168-243e-4e64-87d3-a2b5085a77a2', 'formattedDate': '21/04/2021', 'Serie': '1', 'Vie': '2'},
            {'Date': '1619017490', 'Niveau': '2', 'Allonge': 'True', 'Assis': 'False', 'SessionID': '1e481168-243e-4e64-87d3-a2b5085a77a2', 'formattedDate': '21/04/2021', 'Serie': '1', 'Vie': '2'}
        ]
        self.assertEqual(streaked_data, expected_streak_data)

if __name__ == '__main__':
    unittest.main()
