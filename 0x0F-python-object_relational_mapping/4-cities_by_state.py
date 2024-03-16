#!/usr/bin/python3
"""This script lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()

    sql_query = "SELECT cities.id, cities.name, states.name \
                 FROM cities, states \
                 WHERE cities.state_id = states.id \
                 ORDER BY cities.id"
    cur.execute(sql_query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
