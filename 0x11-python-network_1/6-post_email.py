#!/usr/bin/python3
'''script that fetches `https://alx-intranet.hbtn.io/status` '''
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    r = requests.post(url, data=values)
    print(r.content.decode())
