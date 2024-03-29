#!/usr/bin/python3
"""This is the module that lists all states from MysQl database"""
import sys
import MySQLdb

def list_states(username, password, database):
    # Connects to thee MySQL server
    db = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()

    # Execute the SQL query to fetch all states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    #fetch all the rows from the query result
    rows = cursor.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close the database connection
    db.close()

# Example usage
if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)
