#! /usr/bin/env python

import json
import psycopg2


#import sqlite3
#db = sqlite3.connect('../db.sqlite3')

# db = psycopg2.connect(
#     host="ec2-23-21-236-249.compute-1.amazonaws.com:5432",
#     dbname="d13o8ji4kob0as",
#     user="ckyuocextchdv",
#     password="abd7e1aa626733780addaeeda9c4fd00cfb08f4b87b177eac05db58afbfb6e2e"
#                       )

import urllib.parse as urlparse
import os

url = urlparse.urlparse(os.environ['DATABASE_URL'])
dbname = url.path[1:]
user = url.username
password = url.password
host = url.hostname
port = url.port

db = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
            )

dictionary = json.load(open('dictionary.json'))

#query = "insert into api_dictionary values (%s)"
c = db.cursor()

for word, description in dictionary.items():
    #keys = (word, description)
    c.execute("""insert into api_dictionary values ('%s','%s')""" % (word.replace('"', r'"').replace("'", r"''"),
                                                                     description.replace('"', r'\\"').replace("'", r"''")))
c.close()
db.commit()

