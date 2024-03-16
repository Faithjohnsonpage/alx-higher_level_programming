#!/usr/bin/python3
"""This script takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument."""

import sys
import MySQLdb


if len(sys.argv) == 5:
    if __name__ == '__main__':
        db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3])
        cur = db.cursor()

        # Get state name argument
        state_name = sys.argv[4]

        # Construct the SQL query using format method
        sql_query = "SELECT * FROM states WHERE name LIKE BINARY %s \
                     ORDER BY id"

        cur.execute(sql_query, (state_name,))
        rows = cur.fetchall()
        for row in rows:
            print(row)
