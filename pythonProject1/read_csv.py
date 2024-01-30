import csv

def read_fruits():
    fruits = []
    with open('fruits.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            fruits.append(row[0])
    return fruits