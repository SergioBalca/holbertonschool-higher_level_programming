#!/usr/bin/python3

""" Script that lists all states with a name starting with N from the
    database hbtn_0e_0_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    user_name = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    con = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=user_name,
            passwd=password,
            db=db_name
            )
    cur = con.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    con.close()
