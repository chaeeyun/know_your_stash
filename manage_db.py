import csv
import codecs
import json
import pdb

def convert_csv():
    csvfile = open('stash.csv', 'r')
    jsonfile = open('stash.json', 'w')

    fieldnames = ("Name", "color", "quantitly", "needle", "material", "guage", "yardage", "producer")
    reader = csv.DictReader(csvfile, fieldnames)
    yarndb = dict()
    for row in reader:
        yarndb[row['Name']] = row
    json.dump(yarndb, jsonfile, ensure_ascii=False)

def review_yarndb():
    fo = open('stash.json',)
    stash = json.load(fo)

    for yarn in stash:
        if stash[yarn]['Name']:
            print(stash[yarn])

    fo.close()

if __name__ == '__main__':
    convert_csv()
    review_yarndb()
