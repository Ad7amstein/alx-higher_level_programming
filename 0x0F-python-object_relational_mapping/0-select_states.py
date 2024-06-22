#!/usr/bin/python3
"""Get all states"""

import MySQLdb
import sys


def main():
    """A script that lists all states from the database hbtn_0e_0_usa
    """
    user, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    port = 3306
    host = "localhost"
    db = MySQLdb.connect(
            host=host, user=user, port=port,
            passwd=password, db=database)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
