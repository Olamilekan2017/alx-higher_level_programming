#!/usr/bin/python3
"""
Takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument
But this time, write one that is safe from MySQL injections!"""
import MySQLdb
from sys import argv


def main():
    _user = argv[1]
    _pw = argv[2]
    _dbname = argv[3]
    _sName = argv[4]

    con = MySQLdb.connect(
         host="localhost",
         port=3306,
         user=_user,
         passwd=_pw,
         db=_dbname,
         charset="utf8")
    cursor = con.cursor()
    que = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(que)
    states = cursor.fetchall()
    for state in states:
        if state[1] == _sName:
            print(state)
    cursor.close()
    con.close()


if __name__ == "__main__":
    main()
