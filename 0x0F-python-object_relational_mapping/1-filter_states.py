#!/usr/bin/python3
""" lists all states with name starting with N from database hbtn_0e_0_usa """
import MySQLdb
from sys import argv


if __name__ == "__main__":
    _mysql_username = argv[1]
    _mysql_password = argv[2]
    _database_name = argv[3]

    con = MySQLdb.connect(
         host="localhost",
         port=3306,
         user=_mysql_username,
         passwd=_mysql_password,
         db=_database_name,
         charset="utf8")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    states = cursor.fetchall()
    for state in states:
        if state[1][0] == 'N':
            print(state)
    cursor.close()
    con.close()
