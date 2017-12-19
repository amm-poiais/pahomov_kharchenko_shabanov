#! /usr/bin/env python

import json
import sqlite3

dictionary = json.load(open('../dictionary.json'))
db = sqlite3.connect('../db.sqlite3')
query = "insert into api_dictionary values (?,?)"
c = db.cursor()

for word, description in dictionary.items():
    keys = (word, description)
    c.execute(query, keys)
c.close()
db.commit()

