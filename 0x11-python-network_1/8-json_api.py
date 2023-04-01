#!/usr/bin/python3
'''script that fetches `https://alx-intranet.hbtn.io/status` '''
import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    values = {'q': ""}
    if len(sys.argv) >= 2:
        values = {'q': sys.argv[1]}
    if values['q'] == "":
        print("No result")
        exit()
    r = requests.post(url, data=values)

    try:
        string1 = r.content.decode()
        if string1[0] == '{' and string1[1] == '}':
            print("No result")
            exit()
        string = r.content.decode().split(',')
        string_id = string[0].split(':')[1]
        name = string[1].split(':')[1]
        name = name.split('\n')[0]
        print(f"[{string_id}] {name}")
    except Exception:
        print("Not a valid JSON")
