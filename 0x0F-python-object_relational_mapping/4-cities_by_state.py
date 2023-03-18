#!/usr/bin/python3
'''Connecting a database with python'''
import MySQLdb
import sys


if __name__ == '__main__':
    '''Dont work on import'''

    args = sys.argv

    if (len(args) <= 3):
        exit()

    db = MySQLdb.connect(host='localhost', user=args[1],
                         passwd=args[2], db=args[3])
    cur = db.cursor()

    cur.execute("SELECT id, name, (SELECT name FROM states \
                 WHERE id = state_id) as states FROM cities")
    rows = cur.fetchall()

    for i in rows:
        print(i)
