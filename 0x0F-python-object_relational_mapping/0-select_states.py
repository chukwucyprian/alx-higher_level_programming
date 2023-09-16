#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states")
    rows = cur.fetchall()

    distinct_names = set()
    
    if len(rows) == 0:
        print("No state names found.")
    else:
        print("State names:")
        for row in rows:
            state_id, state_name = row[0], row[1]
            if state_name not in distinct_names:
                print(f"({state_id}, '{state_name}')")
                distinct_names.add(state_name)
    
    cur.close()
    db.close()
