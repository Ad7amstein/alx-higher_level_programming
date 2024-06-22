#!/usr/bin/python3
"""Filter states by user input"""

import MySQLdb
import sys


def main():
    """A script that takes in an argument
    and displays all values in the states table
    of hbtn_0e_0_usa where name matches the argument.
    """
    user, password, database, searched_name =\
        sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    host = "localhost"
    port = 3306
    db = MySQLdb.connect(host=host, port=port, user=user,
                         passwd=password, db=database)
    cur = db.cursor()
    cur.execute("""SELECT * FROM states
                   WHERE states.name LIKE '{}'
                   ORDER BY states.id ASC""".format(searched_name))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
