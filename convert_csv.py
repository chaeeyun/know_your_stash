import csv
import codecs
import json

csvfile = open('stash.csv', 'r')
jsonfile = open('stash.json', 'w')

fieldnames = ("Name", "color", "quantitly", "needle", "material", "guage", "yardage", "producer")
reader = csv.DictReader(csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile, ensure_ascii=False)
    jsonfile.write('\n')
