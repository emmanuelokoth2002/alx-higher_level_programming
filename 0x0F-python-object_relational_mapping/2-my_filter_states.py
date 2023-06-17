#!/usr/bin/python3
"""takes in an argument and displays all values in the states table """

import MySQLdb
from sys import argv

if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost", port=3306,
                                 user=argv[1], passwd=argv[2], db=argv[3])
    cursor = connection.cursor()
    sql = """
    SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY states.id ASC"""
    sql = sql.format(argv[4])
    cursor.execute(sql)
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    cursor.close()
    connection.close()
