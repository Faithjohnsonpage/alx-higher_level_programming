#!/usr/bin/python3
"""This script lists all states from the database hbtn_0e_0_usa"""

import sys
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    # Get state name argument
    state_name = sys.argv[4]

    # Construct the SQL query using format method
    sql_query = "SELECT * FROM states WHERE name = '{}' \
                 ORDER BY id ASC".format(state_name)

    cur.execute(sql_query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
