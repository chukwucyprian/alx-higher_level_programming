#!/usr/bin/python3
"""A script that
- fetches https://alx-intranet.hbtn.io/status.
- uses urlib package
"""


if __name__ == '__main__':
    import urllib.request


    url = 'https://alx-intranet.hbtn.io/status'

    try:
        with urllib.request.urlopen(url) as resp:
            content = resp.read()
            print("Body response:")
            print("\t - type: {}".format(type(content)))
            print("\t - content: {}".format(content))
            print("\t - utf8 content: {}".format(content.decode('utf-8')))
    except Exception as e:
        print("An error occurred:", e)
