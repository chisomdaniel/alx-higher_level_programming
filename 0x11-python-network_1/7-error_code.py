#!/usr/bin/python3
'''fetches a url, using the `request` lib '''
import requests
import sys


if __name__ == '__main__':

    r = requests.get(sys.argv[1])

    if r.status_code >= 400:
        print("Error code:", r.status_code)
    else:
        print(r.content.decode())
