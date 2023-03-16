import time
import requests
from threading import Thread
from datetime import datetime


def get_html(link):
    response = requests.get(link)
    #response.text
    print(response.text)


S = ['https://google.com', 'https://rbc.ru', 'https://dzen.ru', 'https://wowhead.com', 'https://github.com']
t0 = datetime.now()
for i in S:
    get_html(i)
print('время выполнения ', (datetime.now() - t0).microseconds, 'мксек')

t1 = datetime.now()
threads = [Thread(target = get_html, args = (i, )) for i in S]
for t in threads:
        t.start()
for t in threads:
        t.join()
print('время выполнения ', (datetime.now() - t1).microseconds, 'мксек')

