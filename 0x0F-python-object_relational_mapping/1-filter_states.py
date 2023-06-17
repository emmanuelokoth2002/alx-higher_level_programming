#!/usr/bin/python3
""" lists all states with a name starting with N"""

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./1-filter_states.py < mysql_username >
              <mysql_password > < database_name >")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

        cursor = db.cursor()

        cursor.execute("SELECT * FROM states
                       WHERE name LIKE 'N%' ORDER BY id ASC")

        rows = cursor.fetchall()

        for row in rows:
            print(row)

        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
        sys.exit(1)
