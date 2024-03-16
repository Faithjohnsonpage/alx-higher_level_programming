#!/usr/bin/python3
"""This script takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa"""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()

    state_name = argv[4]

    sql_query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name LIKE BINARY %s
        ORDER BY cities.id
    """
    cur.execute(sql_query, (state_name,))
    rows = cur.fetchall()
    if rows is not None:
        print(", ".join([row[0] for row in rows]))
