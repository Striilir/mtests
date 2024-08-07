# Rendu de méthodo de tests Titouan REYNAUD

## Description

Le projet comprend deux scripts Bash et Python pour traiter un fichier CSV d'exercices et calculer des séries pour chaque utilisateur. On retrouve aussi des tests pour assurer la qualité des scripts.

### Contenu du répo

- `process_csv.sh` : Le script principal qui permet de lancer le traitement des données.
- `process_csv.py`: Un script en Python qui fait le gros du traitement du CSV, calcul des séries et des vies.
- `run_tests.sh` : Un script pour exécuter les tests unitaires et vérifier les résultats.
- `Enregistrement.csv` : Un fichier CSV à traiter.
- `test_process_csv.py` : Un script de tests unitaires pour vérifier le bon fonctionnement du traitement du CSV.

### Prérequis avant de lancer les scripts

Assurez-vous d'avoir les éléments suivants installés sur votre système :

- Bash
- Python 3
- Avoir rendu les scripts exécutables avec `chmod +x nom_du_script.sh`
```bash
chmod +x process_csv.sh
chmod +x run_tests.sh
```

## Instructions

### Exécuter le script de traitement des données

*Paramètres:*
- `-f` : Fichier CSV d'entrée.
- `-o` : Fichier CSV de sortie.
- `-n` : (Optionnel) Nombre de lignes à traiter à partir du fichier d'entrée.

Exécutez le script principal `process_csv.sh` avec le fichier de test généré comme argument :

```bash
./process_csv.sh -f Enregistrement.csv -o output.csv
```

### Exécuter les tests unitaires
Exécutez le script de test unitaire run_tests.sh pour vérifier les résultats :
```bash
./run_tests.sh
```
