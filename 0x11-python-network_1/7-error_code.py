#!/usr/bin/python3
"""A script that
- takes in a URL
- sends a request to the URL
- displays the body of the response.
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        response = requests.get(url)
        response.raise_for_status()

        print(response.text)
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
    except requests.exceptions.HTTPError as e:
        print("Error code:", e.response.status_code)
