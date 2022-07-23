#!/usr/bin/env python

import csv
import sqlalchemy

# connect to the database
engine = sqlalchemy.create_engine("postgresql://codetest:password@database/codetest")
connection = engine.connect()

metadata = sqlalchemy.schema.MetaData(engine)

# make an ORM object to refer to the table
Places = sqlalchemy.schema.Table('places', metadata, autoload=True, autoload_with=engine)
People = sqlalchemy.schema.Table('people', metadata, autoload=True, autoload_with=engine)

# insert data into places table
with open('/data/places.csv') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)
    for row in reader:
        connection.execute(Places.insert().values(city=row[0], county=row[1], country=row[2]))


places = connection.execute(sqlalchemy.sql.select([Places])).fetchall()

# build diction of places id and city name using one-liner
places_dict = {place[1]: place[0] for place in places}

# insert data into people table
with open('/data/people.csv') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)
    for row in reader:
        connection.execute(People.insert().values(given_name=row[0], family_name = row[1], date_of_birth = row[2],
                                                  place_of_birth=places_dict[row[3]]))
