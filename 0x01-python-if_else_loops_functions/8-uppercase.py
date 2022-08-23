#!/usr/bin/python3

def uppercase(str):
    new = ''
    for letter in str:
        num = ord(letter)
        if num >= 97 and num <= 122:
            new += chr(num - 32)
        else:
            new += letter
    print("{}".format(new))
