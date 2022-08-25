#!/usr/bin/python3
import sys

argv = sys.argv
length = len(argv)

if __name__ == "__main__":

    if length == 1:
        print("0 arguments.")
        sys.exit()
    if length == 2:
        print("1 argument:")
    if length > 2:
        print("{} arguments:".format(length - 1))

    i = 1
    while i < length:
        print("{}: {}".format(i, argv[i]))
        i += 1
