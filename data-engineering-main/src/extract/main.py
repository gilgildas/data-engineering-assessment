#!/usr/bin/env python

import json
import sqlalchemy

# connect to the database
engine = sqlalchemy.create_engine("postgresql://codetest:password@database/codetest")
connection = engine.connect()

metadata = sqlalchemy.schema.MetaData(engine)

# sql query for aggregation of total people by country
result = connection.execute("""
    SELECT c.country, count(*) as total from people as p LEFT JOIN places as c ON p.place_of_birth = c.id GROUP BY c.country;
""").fetchall()

# output the aggregation results to a JSON file
with open('/data/summary_output.json', 'w') as json_file:
    rows = {}
    for row in result:
        rows[row[0]] = row[1]
    json.dump(rows, json_file, separators=(',', ':'))
