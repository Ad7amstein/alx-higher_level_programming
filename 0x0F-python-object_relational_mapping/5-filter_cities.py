#!/usr/bin/python3
"""All cities by state"""

import MySQLdb
import sys


def main():
    """A script that takes in the name of a state
    as an argument and lists all cities of that state,
    using the database hbtn_0e_4_usa
    """
    user, password, database, state_name =\
        sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    db = MySQLdb.connect(host="localhost", passwd=password, user=user,
                         port=3306, db=database)
    cur = db.cursor()
    cur.execute("""SELECT c.id, c.name, s.name
                   FROM cities AS c, states AS s
                   WHERE s.id = c.state_id
                   AND s.name = %s
                   ORDER BY c.id ASC""", (state_name,))
    rows = cur.fetchall()
    i = 0
    for row in rows:
        if i:
            print(', ', end='')
        print(row[1], end='')
        i += 1
    print()

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
