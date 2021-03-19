import csv

with open('D:\\Python\\Kaggle\\Titanic\\train.csv', 'r') as f:
    r = csv.reader(f, delimiter=',')
    for row in r:
        print(','.join(row))