import csv
import sqlite3


con = sqlite3.connect('titanic.db')
cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS people(
name TEXT,
age INT,
job TEXT,
survived TEXT);""")

with open('titanic.csv') as csvfile:
    data = csv.reader(csvfile)
    for line in data:
        person = (line[0], line[1], line[5], line[6])
        cur.execute("""INSERT INTO people VALUES(?, ?, ?, ?)""", person)
con.commit()
    