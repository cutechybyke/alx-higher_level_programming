#!/usr/bin/python3
"""Module that lists all states from htbn"""

import sys
import MySQLdb

if __name__== "__main__":
    # Get MySQL credentials and search name from command-line
    db = MySQLdb.connect (user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    # Connect to MySQL server
    c = db.cursor()

      # Execute the SQL query to retrieve all states
    c.excute("SELECT `c`.`id`, `c`.name`, `s`.`name` \
                FROM `cities` as `c` \
               INNER JOIN `states` as `s` \
                ON `c`.`state_id` = `s`.`id` \
               ORDER BY `c`.`id`")

    # Fetch all rows and print the states
    [print(city) for city in city c.fetchall()]
