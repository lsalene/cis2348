##Leira Salene 1785752

import csv

data_dict = {}
fileName = input()
with open(fileName, newline='') as f:
    reader = csv.reader(f)
    for lineArray in reader:
        for key in lineArray:
            if key in data_dict:
                data_dict[key] = data_dict[key] + 1
            else:
                data_dict[key] = 1
for key, count in data_dict.items():
    print(key, count)
