import csv
from datetime import datetime, timedelta
from itertools import groupby
import argparse
import os

def read_csv(filename):
    with open(filename, mode='r') as infile:
        reader = csv.DictReader(infile)
        data = [row for row in reader]
    return data

def write_csv(data, filename):
    os.makedirs(os.path.dirname(filename) or '.', exist_ok=True)
    
    fieldnames = ['Date', 'Niveau', 'Allonge', 'Assis', 'SessionID', 'formattedDate', 'Serie', 'Vie']
    
    with open(filename, mode='w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        for row in data:
            filtered_row = {field: row.get(field, '') for field in fieldnames}
            writer.writerow(filtered_row)

def clean_input_data(data):
    cleaned_data = []
    for row in data:
        date = datetime.fromtimestamp(int(row['Date']))
        row['formattedDate'] = date.strftime('%d/%m/%Y')
        cleaned_data.append(row)
    return cleaned_data

def streak_user(data):
    users = set(row['SessionID'] for row in data)
    for user in users:
        user_data = [row for row in data if row['SessionID'] == user]
        user_data.sort(key=lambda x: datetime.strptime(x['formattedDate'], '%d/%m/%Y'))
        current_streak = 0
        lives = 2
        days_data = [(day, list(day_data)) for day, day_data in groupby(user_data, lambda x: x['formattedDate'])]
        min_date = datetime.strptime(min(user_data, key=lambda x: datetime.strptime(x['formattedDate'], '%d/%m/%Y'))['formattedDate'], '%d/%m/%Y')
        max_date = datetime.strptime(max(user_data, key=lambda x: datetime.strptime(x['formattedDate'], '%d/%m/%Y'))['formattedDate'], '%d/%m/%Y')
        for currentDay in (min_date + timedelta(n) for n in range((max_date - min_date).days + 1)):
            time_assis = 0
            time_allonge = 0
            exercice_done = False
            for day, day_data in days_data:
                if datetime.strptime(day, '%d/%m/%Y') == currentDay:
                    for row in day_data:
                        if row['Assis'] == 'True':
                            time_assis += 10 if row['Niveau'] == '2' else 5 if row['Niveau'] == '1' else 0
                        if row['Allonge'] == 'True':
                            time_allonge += 10 if row['Niveau'] == '2' else 5 if row['Niveau'] == '1' else 0
                        if time_assis >= 10 and time_allonge >= 10 and not exercice_done:
                            exercice_done = True
                            current_streak += 1
                            if current_streak % 5 == 0:
                                lives = min(lives + 1, 2)
                        row['Serie'] = str(current_streak)
                        row['Vie'] = str(lives)
            if not exercice_done:
                if current_streak > 0:
                    lives -= 1
                if lives == 0:
                    current_streak = 0
                    lives = 2
    return data

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="input file")
    parser.add_argument("-o", "--output", help="output file")
    parser.add_argument("-n", "--lines", type=int, help="number of lines to process")
    args = parser.parse_args()

    if not args.file:
        print('Veuillez spécifier un fichier d\'entrée')
        exit()
    
    data = read_csv(args.file)
    if args.lines:
        data = data[:args.lines]
    cleaned_data = clean_input_data(data)
    streak_data = streak_user(cleaned_data)
    if args.output:
        write_csv(streak_data, args.output)
    else:
        write_csv(streak_data, './output.csv')
