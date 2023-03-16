import time
from threading import Thread
from datetime import datetime


def get_thread(thread_name):
    time.sleep(1)
    print(f'процесс {thread_name} ')

S = ['thread 1', 'thread 2', 'thread 3', 'thread 4', 'thread 5']
t0 = datetime.now()
for i in S:
    get_thread(i)
print('время выполнения ', (datetime.now() - t0).seconds, 'сек')

t1 = datetime.now()
threads = [Thread(target = get_thread, args = (i, )) for i in S]
for t in threads:
        t.start()
for t in threads:
        t.join()
print('время выполнения ', (datetime.now() - t1).seconds, 'сек')


