#!/usr/bin/python3
import sys

argv = sys.argv
length = len(argv)

if __name__ == "__main__":

    if length == 1:
        print("0")
        sys.exit()

    total = 0
    i = 1
    while i < length:
        total += int(argv[i])
        i += 1

    print(total)
