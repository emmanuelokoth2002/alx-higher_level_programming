#!/usr/bin/python3
"""Lists all states with safe MySQL query"""

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./safe_states.py [username] [password] [database] [state_name]")
        sys.exit(1)

    username = MySQLdb.escape_string(sys.argv[1])
    password = MySQLdb.escape_string(sys.argv[2])
    database = MySQLdb.escape_string(sys.argv[3])
    state_name = MySQLdb.escape_string(sys.argv[4])

    try:
        connection = MySQLdb.connect(host="localhost", port=3306,
                                     user=username, passwd=password, db=database)
        cursor = connection.cursor()
        sql = "SELECT * FROM states WHERE name=%s ORDER BY states.id ASC"
        cursor.execute(sql, (state_name,))
        query_rows = cursor.fetchall()
        for row in query_rows:
            print(row)
        cursor.close()
        connection.close()
    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)
