#!/usr/bin/python3
"""Lists all states where name matches the argument"""
# importing dependencies sysarg, mysql connector
import sys
import MySQLdb

if __name__ == "__main__":

    # taking in args, assigning variables
    if len(sys.argv) != 5:
        print(
            f"Usage: {sys.argv[0]} <db_user> <db_password> <db_name> <state>"
            )
        sys.exit(1)

    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    find_state = sys.argv[4]

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
        "SELECT * "
        "FROM states "
        "WHERE BINARY name = '{}' "
        "ORDER BY id ASC".format(find_state)
        )
    # retrieving results as query_rows
    query_rows = cur.fetchall()
    # printing each row in query_rows e.g. results of db connection
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
