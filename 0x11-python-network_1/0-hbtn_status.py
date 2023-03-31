#!/usr/bin/python3
'''script that fetches `https://alx-intranet.hbtn.io/status` '''
import urllib.request


with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()
    print("Body response:")
    print("    -", type(html))
    print("    -", html)
    print("    -", html.decode())
