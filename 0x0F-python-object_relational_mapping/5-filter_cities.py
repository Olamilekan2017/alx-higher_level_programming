#!/usr/bin/python3
"""
Lists all cities of that state, using the database hbtn_0e_4_usa.
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
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
    cursor.execute("SELECT `c`.`id`, `c`.`name`, `s`.`name` \
                FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                   ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")
    cities = cursor.fetchall()

    theCities = ''

    for city in cities:
        if city[2] == _sName:
            theCities += city[1] + ', '

    print(theCities[:-2])
    cursor.close()
    con.close()
