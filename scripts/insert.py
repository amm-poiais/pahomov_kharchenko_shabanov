#! /usr/bin/env python

import json
import psycopg2


#import sqlite3
#db = sqlite3.connect('../db.sqlite3')

db = psycopg2.connect('postgresql-fitted-67108')
dictionary = json.load(open('dictionary.json'))

query = "insert into api_dictionary values (?,?)"
c = db.cursor()

for word, description in dictionary.items():
    keys = (word, description)
    c.execute(query, keys)
c.close()
db.commit()

