import time
from threading import Thread, local


#
# def main():
#     msg = input(" ")
#     results = requests.get(f'http://127.0.0.1:8000/{msg}')
#     jresults = results.json()
#     print(jresults['message'])
#     main()
#
#
# main()
import requests


class Spammer(Thread):
    def __init__(self, url):
        Thread.__init__(self)
        self.url = url

    def run(self):
        while True:
            try:
                response = requests.get(self.url)
                print(f"Sent GET request to {self.url} ({response.text})")
            except:
                time.sleep(0.1)
                continue



def main():
    url = input('Insert url: ')
    threads = []
    threads_n = int(input('Insert number of threads: '))
    for _ in range(threads_n):
        new_spammer = Spammer(url)
        new_spammer.start()
        threads.append(new_spammer)


if __name__ == '__main__':
    main()
