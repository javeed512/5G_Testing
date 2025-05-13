
import csv
import json

from json2xml import json2xml

with open('file_data_formats/input.csv', mode='r', newline='', encoding='utf-8') as csvfile:
    data = list(csv.DictReader(csvfile))
print(data)


with open('output.json', mode='w', encoding='utf-8') as jsonfile:
    json.dump(data, jsonfile, indent=4)


            




