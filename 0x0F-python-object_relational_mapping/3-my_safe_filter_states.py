#!/usr/bin/python3

"""Module for lists """
import sys
import MysSQLdb

if __name__== "__main__":
    import MySQLdb
    import sys

    # Get the command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Creata a cursor object to be execute queries
    cursor = db.cursor()

    # Prepare the SQL query with placeholders
    sql_query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    # Execute the query with state name
    cursor.execute(sql_query, (state_name,))

    # fetch all the rows returned by the query
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)
