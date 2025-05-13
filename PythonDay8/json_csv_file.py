
import json
import csv

with open('output.json') as jf:
    d = json.load(jf)

Ed = d['customer_details']

df = open('data_file.csv', 'w')

cw = csv.writer(df)

c = 0

for emp in Ed:
    if c == 0:

        # Writing headers of CSV file
        h = emp.keys()
        cw.writerow(h)
        c += 1

    # Writing data of CSV file
    cw.writerow(emp.values())

df.close()