import json

import requests


def main():
    msg = input(" ")
    results = requests.get(f'http://127.0.0.1:8000/{msg}')
    jresults = results.json()
    print(jresults['message'])
    main()


main()
