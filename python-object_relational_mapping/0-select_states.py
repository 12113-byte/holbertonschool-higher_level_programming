#!/usr/bin/python3
# importing dependencies sysarg, mysql connector
import sys
import MySQLdb
# taking in args, assigning variables
if len(sys.argv) != 4:
    print(f"Usage: {sys.argv[0]} <db_user> <db_password> <db_table>")
    sys.exit(1)

db_user = sys.argv[1]
db_password = sys.argv[2]
db_table = sys.argv[3]

# simple database connection script
# localhost connection port 3306
conn = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=db_user,
    passwd=db_password,
    db=db_table,
    charset="utf8"
    )
cur = conn.cursor()
# execute sql query on target database
cur.execute("SELECT * FROM states ORDER BY id ASC")
# retrieving results as query_rows
query_rows = cur.fetchall()
# printing each row in query_rows e.g. results of db connection
for row in query_rows:
    print(row)
cur.close()
conn.close()
