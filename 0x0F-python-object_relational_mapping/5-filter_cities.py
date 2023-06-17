#!/usr/bin/python3
"""Lists all cities of a state from hbtn_0e_4_usa database"""

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./5-filter_cities.py [username] [password] [database] [state]")
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
        SELECT GROUP_CONCAT(cities.name SEPARATOR ', ')
        FROM cities
        INNER JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        GROUP BY states.name
        """
        cursor.execute(sql, (state,))
        query_row = cursor.fetchone()
        if query_row:
            cities = query_row[0]
            print(cities)
        else:
            print("No cities found for the given state.")
        cursor.close()
        connection.close()
    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)
