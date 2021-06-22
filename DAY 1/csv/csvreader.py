import csv

with open('addresses.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        print(line)