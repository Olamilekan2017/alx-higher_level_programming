#!/usr/bin/python3
"""
List all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    _user = argv[1]
    _pw = argv[2]
    _dbname = argv[3]

    con = MySQLdb.connect(
         host="localhost",
         port=3306,
         user=_user,
         passwd=_pw,
         db=_dbname,
         charset="utf8")
    cursor = con.cursor()
    cursor.execute("SELECT `c`.`id`, `c`.`name`, `s`.`name` \
                FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                   ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")
    cities = cursor.fetchall()
    for city in cities:
        print(city)
    cursor.close()
    con.close()
