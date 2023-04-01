#!/usr/bin/python3
'''fetches a url, using the `request` lib '''
import requests


if __name__ == '__main__':

    r = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type:", type(r.content.decode()))
    print("\t- content:", r.content.decode())
