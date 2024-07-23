import unittest
import os
import csv
from process_csv import read_csv, write_csv, clean_input_data, streak_user

class TestProcessCSV(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n=== Début des tests pour le module process_csv ===\n")

    @classmethod
    def tearDownClass(cls):
        print("\n=== Fin des tests pour le module process_csv ===\n")

    def setUp(self):
        self.input_file = 'mock_data.csv'
        self.output_file = 'output.csv'
        self.cleaned_data = [
            {'Date': '1618937885', 'Niveau': '2', 'Allonge': 'True', 'Assis': 'True', 'SessionID': 'ed73e2a7-8f8a-493c-9388-c7cc4714b0ad', 'formattedDate': '20/04/2021'},
            {'Date': '1618937885', 'Niveau': '2', 'Allonge': 'True', 'Assis': 'True', 'SessionID': 'ed73e2a7-8f8a-493c-9388-c7cc4714b0ad', 'formattedDate': '20/04/2021'},
            {'Date': '1618937885', 'Niveau': '2', 'Allonge': 'True', 'Assis': 'False', 'SessionID': 'ed73e2a7-8f8a-493c-9388-c7cc4714b0ad', 'formattedDate': '20/04/2021'},
            {'Date': '1618937885', 'Niveau': '2', 'Allonge': 'True', 'Assis': 'True', 'SessionID': 'ed73e2a7-8f8a-493c-9388-c7cc4714b0ad', 'formattedDate': '20/04/2021'},
            {'Date': '1618937885', 'Niveau': '1', 'Allonge': 'True', 'Assis': 'False', 'SessionID': 'ed73e2a7-8f8a-493c-9388-c7cc4714b0ad', 'formattedDate': '20/04/2021'}
        ]
        self.expected_output_data = [
            {'Date': '1618937885', 'Niveau': '2', 'Allonge': 'True', 'Assis': 'True', 'SessionID': 'ed73e2a7-8f8a-493c-9388-c7cc4714b0ad', 'formattedDate': '20/04/2021', 'Serie': '1'},
            {'Date': '1618937885', 'Niveau': '2', 'Allonge': 'True', 'Assis': 'True', 'SessionID': 'ed73e2a7-8f8a-493c-9388-c7cc4714b0ad', 'formattedDate': '20/04/2021', 'Serie': '1'},
            {'Date': '1618937885', 'Niveau': '2', 'Allonge': 'True', 'Assis': 'False', 'SessionID': 'ed73e2a7-8f8a-493c-9388-c7cc4714b0ad', 'formattedDate': '20/04/2021', 'Serie': '1'},
            {'Date': '1618937885', 'Niveau': '2', 'Allonge': 'True', 'Assis': 'True', 'SessionID': 'ed73e2a7-8f8a-493c-9388-c7cc4714b0ad', 'formattedDate': '20/04/2021', 'Serie': '1'},
            {'Date': '1618937885', 'Niveau': '1', 'Allonge': 'True', 'Assis': 'False', 'SessionID': 'ed73e2a7-8f8a-493c-9388-c7cc4714b0ad', 'formattedDate': '20/04/2021', 'Serie': '1'}
        ]

    def test_read_csv(self):
        """Test de la lecture du fichier CSV"""
        print("Test de la lecture du fichier CSV")
        data = read_csv(self.input_file)
        self.assertEqual(len(data), 5, "Le nombre de lignes lues doit être 5")
        self.assertEqual(data[0]['Date'], '1618937885', "La première date doit être 1618937885")
        self.assertEqual(data[0]['Niveau'], '2', "Le premier niveau doit être 2")

    def test_write_csv(self):
        """Test de l'écriture du fichier CSV"""
        print("Test de l'écriture du fichier CSV")
        updated_data = streak_user(self.cleaned_data)  # Update streaks before writing
        write_csv(updated_data, self.output_file)
        self.assertTrue(os.path.exists(self.output_file), "Le fichier de sortie doit exister")

        with open(self.output_file, mode='r') as infile:
            reader = csv.DictReader(infile)
            output_data = [row for row in reader]

        self.assertEqual(output_data, self.expected_output_data, "Les données écrites ne correspondent pas aux données attendues")

    def test_clean_input_data(self):
        """Test de nettoyage des données d'entrée"""
        print("Test de nettoyage des données d'entrée")
        cleaned_data = clean_input_data(self.cleaned_data)
        self.assertEqual(cleaned_data[0]['formattedDate'], '20/04/2021', "La date formatée doit être 20/04/2021")

    def test_streak_user(self):
        """Test de la fonction de calcul des séries utilisateur"""
        print("Test de la fonction de calcul des séries utilisateur")
        streaked_data = streak_user(self.cleaned_data)
        self.assertEqual(streaked_data, self.expected_output_data, "Les données de séries ne correspondent pas aux données attendues")

if __name__ == '__main__':
    unittest.main(verbosity=2)
