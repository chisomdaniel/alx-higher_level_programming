#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":

    argv = sys.argv
    length = len(argv)

    if length == 4:
        sign = argv[2]
        if sign == '+':
            answer = add(int(argv[1]), int(argv[3]))
        elif sign == '-':
            answer = sub(int(argv[1]), int(argv[3]))
        elif sign == '*':
            answer = mul(int(argv[1]), int(argv[3]))
        elif sign == '/':
            answer = div(int(argv[1]), int(argv[3]))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    print("{} {} {} = {}".format(argv[1], sign, argv[3], answer))
