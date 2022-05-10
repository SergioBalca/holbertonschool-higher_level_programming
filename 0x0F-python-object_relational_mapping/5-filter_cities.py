#!/usr/bin/python3

""" Takes arguments and displays all values in the states table
    of hbtn_0e_0_usa where name matches the argument, safe
    from MySQL injections
"""

import sys
import MySQLdb

if __name__ == "__main__":
    user_name = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state = sys.argv[4]

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
    cur.execute("""SELECT cities.name
                FROM cities INNER JOIN states
                ON cities.state_id = states.id
                WHERE states.name = %(states.name)s
                ORDER BY cities.id ASC""", {'states.name': state})

    """ Fetchall to get the results """
    rows = cur.fetchall()
    print(str(', '.join(row[0] for row in rows)))
    cur.close()
    con.close()
