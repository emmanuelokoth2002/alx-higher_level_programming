#!/usr/bin/python3
"""Lists all cities of a state from hbtn_0e_4_usa database"""

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./4-cities_by_state.py [username] [password] [database] [state]")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    try:
        connection = MySQLdb.connect(host="localhost", port=3306,
                                     user=username, passwd=password, db=database)
        cursor = connection.cursor()
        sql = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        INNER JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """
        cursor.execute(sql, (state,))
        query_rows = cursor.fetchall()
        for row in query_rows:
            print(row)
        cursor.close()
        connection.close()
    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)
