#!/usr/bin/python3

""" Script that lists all states from the database hbtn_0e_0_usa
    in ascending order by state id
"""

import sys
import MySQLdb

user_name = sys.argv[1]
password = sys.argv[2]
db_name = sys.argv[3]


""" To connect to the MYSQL server on port 3306 (default) """
con = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user_name,
        passwd=password,
        db=db_name
     )

""" To get a cursor """
cur = con.cursor()
cur.execute("SELECT states.id, states.name FROM states ORDER BY states.id ASC")

""" Fetchall to get the results """
rows = cur.fetchall()
for row in rows:
    print(row)
cur.close()
con.close()

if __name__ == "0-select_states":
    0-select_states()
