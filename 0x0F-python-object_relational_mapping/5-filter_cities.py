#!/usr/bin/python3
'''Connecting a database with python'''
import MySQLdb
import sys


if __name__ == '__main__':
    '''Dont work on import'''

    args = sys.argv

    if (len(args) <= 4):
        exit()

    db = MySQLdb.connect(host='localhost', user=args[1],
                         passwd=args[2], db=args[3])
    cur = db.cursor()

    cur.execute("SELECT name FROM cities WHERE state_id = \
                 (SELECT id FROM states WHERE name = %s)", (args[4],))
    rows = cur.fetchall()

    count = 0
    for i in rows:
        print(f"{i[0]}", end="")
        count += 1
        if (count != len(rows)):
            print(", ", end="")
    print("")
