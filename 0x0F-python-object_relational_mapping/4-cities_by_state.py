#!/usr/bin/python3
"""Cities by states"""

import MySQLdb
import sys


def main():
    """A script that lists all cities from the database hbtn_0e_4_usa
    """
    user, password, database =\
        sys.argv[1], sys.argv[2], sys.argv[3]
    db = MySQLdb.connect(user=user, passwd=password,
                         host="localhost", port=3306, db=database)
    cur = db.cursor()
    cur.execute("""SELECT c.id, c.name, s.name
                   FROM cities AS c, states AS s
                   WHERE c.state_id = s.id
                   ORDER BY c.id ASC""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
