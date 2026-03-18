#!/usr/bin/python3
"""Lists all cities from the database"""
# importing dependencies sysarg, mysql connector
import sys
import MySQLdb

if __name__ == "__main__":

    # taking in args, assigning variables
    if len(sys.argv) != 4:
        print(
            f"Usage: {sys.argv[0]} <db_user> <db_password> <db_name>"
            )
        sys.exit(1)

    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]

    # simple database connection script
    # localhost connection port 3306
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=db_user,
        passwd=db_password,
        db=db_name,
        charset="utf8"
        )
    cur = conn.cursor()
    # execute sql query on target database
    cur.execute(
        "SELECT cities.id, cities.name, states.name "
        "FROM cities "
        "INNER JOIN states ON states.id = cities.state_id "
        "ORDER BY cities.id ASC"
        )
    # retrieving results as query_rows
    query_rows = cur.fetchall()
    # printing each row in query_rows e.g. results of db connection
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
