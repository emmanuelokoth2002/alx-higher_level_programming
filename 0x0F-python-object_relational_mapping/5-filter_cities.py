#!/usr/bin/python3
"""Lists all cities of a given state from the database hbtn_0e_4_usa"""

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()

    query = """
        SELECT cities.name
        FROM cities
        INNER JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))

    rows = cursor.fetchall()

    cities = [row[0] for row in rows]

    print(", ".join(cities))

    cursor.close()
    db.close()
