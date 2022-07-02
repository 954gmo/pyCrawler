# -*- encoding:utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__ENTITY_author__ = "SIX DIGIT INVESTMENT GROUP"
__author__ = "GWONGZAN"

import multiprocessing

"""
os.fork , only Unix/Linux
multiprocessing, cross platform

communication between processes
Pipe ( 2 processes)
    duplex(True/ False)
Queue ( 2+ processes) 
    Put: blocked (True/ False), timeout, Queue.Full
    Get: blocked (True/ False), timeout, Queue.Empty
    
thread and threading    


GIL and I/O: thread, CPU : process

coroutine and gevent

distribution multi process

分布式进程
1. create queue for IPC, service process create task_queue, result_queue, add task to Queue via Queuemanager
2. register the Queue and explode to other host
3. 
"""

import os, time, random
from multiprocessing import Process, Pool, Queue
import threading
from gevent import monkey
monkey.patch_all()
from gevent.pool import Pool as GPool
import gevent
from urllib3 import PoolManager
import urllib3
from functools import partial

from Util import FontColor





def run_sub_proc(name):
    print('Child Process {} ({}) running ... '.format(name, os.getpid()))


def run_task(name):
    print(f"Task {name} ({os.getpid()}) is running...")
    time.sleep(random.random() * 4)
    print(f"Task {name} end")


def multi_process():
    print(f"{FontColor.CYAN}Parent Process {os.getpid()}  ")
    for i in range(5):
        p = Process(target=run_sub_proc, args=(str(i),))
        print('Process will start')
        p.start()
    p.join()
    print("process end")


def process_pool():
    print(f"{FontColor.GREEN}Current process {os.getpid()}")
    p = Pool(processes=3)
    for i in range(13):
        p.apply_async(run_task, args=(i,))
    print("waiting for all subprocess done...")
    p.close()
    p.join()
    print("all process done")


def proc_write(q, urls):
    print(f"Process {os.getpid()} is writing ....")
    for url in urls:
        q.put(url)
        print(f"Put {url} to queue")
        time.sleep(random.random())


def proc_read(q):
    print(f"Process {os.getpid()} is reading ....")
    while True:
        url = q.get(True)
        print(f'Get {url} from queue ')


def proc_com():
    print(f"{FontColor.BLUE}multi process communication {os.getpid()}... ")
    q = Queue()
    proc_writer1 = Process(target=proc_write, args=(q, ['url1', "url 2", 'url 3']))
    proc_writer2 = Process(target=proc_write, args=(q, ['url4', 'url 5', 'url 6']))
    proc_reader = Process(target=proc_read, args=(q,))

    proc_writer1.start()
    proc_writer2.start()
    proc_reader.start()

    proc_writer1.join()
    proc_writer2.join()
    proc_reader.terminate()


def proc_send(pipe, urls):
    for url in urls:
        print(f"{FontColor.MAGENTA} Process {os.getpid()} send : {url}")
        pipe.send(url)
        time.sleep(random.random())


def proc_recv(pipe):
    while True:
        print(f"Process {os.getpid()} rev: {pipe.recv()}")
        time.sleep(random.random())


def pipe_comm():
    p = multiprocessing.Pipe()
    sender = Process(target=proc_send, args=(p[0], [f'url {i}' for i in range(10)]))
    receiver = Process(target=proc_recv, args=(p[1],))

    sender.start()
    receiver.start()

    sender.join()
    # receiver.join()
    receiver.terminate()


def func_thread(urls):
    print(f"{FontColor.CYAN} current {threading.current_thread().name} is running ... ")
    for url in urls:
        print(f" {threading.current_thread().name} ---->>> {url}")
        time.sleep(random.random())
    print(f"{threading.current_thread().name} ended. ")


def run_thread():
    print(f"{FontColor.GREEN} {threading.current_thread().name} is running")
    t = threading.Thread(target=func_thread, name="Thread_1", args=([f"url {i}" for i in range(10)],))
    t2 = threading.Thread(target=func_thread, name="Thread_2", args=([f'URL {i}' for i in range(30, 50)],))

    t.start()
    t2.start()

    t.join()
    t2.join()

    print(f"{threading.current_thread().name} ended")


class myThread(threading.Thread):
    def __init__(self, name, urls):
        threading.Thread.__init__(self, name=name)
        self.urls = urls

    def run(self):
        print(f"Current {threading.current_thread().name} is running")
        for url in self.urls:
            print(f" {threading.current_thread().name} ---->>> {url}")
            time.sleep(random.random())
        print(f"{threading.current_thread().name} ended. ")


def run_thread_class():
    t = myThread(name="1st Thread", urls=[f"url {i}" for i in range(5)])
    t2 = myThread(name='2nd Thread', urls=[f'url {i}{i}' for i in range(6, 10)])

    t.start()
    t2.start()

    t.join()
    t.join()


my_thread_lock = threading.RLock()
cnt = 0


class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self, name=name)

    def run(self):
        global cnt
        while True:
            my_thread_lock.acquire()
            print(f"{threading.current_thread().name} locked, number {cnt}")
            if cnt >= 4:
                my_thread_lock.release()
                print(f"{threading.current_thread().name} released, number: {cnt}")
                break
            cnt += 1
            print(f"{threading.current_thread().name} released, number: {cnt}")
            my_thread_lock.release()


def run_MyThread_class():
    t1 = MyThread("first thread")
    t2 = MyThread("second thread")

    t1.start()
    t2.start()

    t1.join()
    t2.join()


def coroutine_task(url, url_manager):
    print(f"Visit --> {url}")
    try:
        response = url_manager.request('GET', url)
        data = response.data
        print(f"{len(data)} bytes received from {url}")
    except Exception as e:
        print(e)


http = PoolManager(3)


def coroutine_task_pool(url):
    print(f"Visit --> {url}")
    global http
    try:
        r = http.request('GET', url)
        data = r.data
        print(f"{len(data)} bytes received from {url}")
    except Exception as e:
        print(e)

    return f"url:{url} -->finished"


def run_coroutine_task():
    url_manager = PoolManager()
    urls = ['https://github.com/', 'https://www.python.org/', 'http://www.cnblogs.com/']
    greenlets = [gevent.spawn(coroutine_task, url, url_manager) for url in urls]
    gevent.joinall(greenlets)


def run_coroutine_task_pool():
    pool = GPool(2)
    # url_manager = PoolManager()
    urls = ['https://github.com/', 'https://www.python.org/', 'http://www.cnblogs.com/']
    res = pool.map(coroutine_task_pool, urls)

    print(res)


def coroutine_task_partial(url, url_manager):
    print(f"Visit --> {url}")
    try:
        response = url_manager.request('GET', url)
        data = response.data
        print(f"{len(data)} bytes received from {url}")
    except Exception as e:
        print(e)

    return f"url:{url} -->finished"


def run_coroutine_task_partial():
    ctp = partial(coroutine_task_partial, url_manager=PoolManager(3))
    pool = GPool(2)
    # url_manager = PoolManager()
    urls = ['https://github.com/', 'https://www.python.org/', 'http://www.cnblogs.com/']
    res = pool.map(ctp, urls)

    print(res)


if __name__ == "__main__":
    # multi_process()
    # process_pool()
    # proc_com()
    # pipe_comm()
    # run_thread()
    # run_thread_class()
    # run_MyThread_class()
    # run_coroutine_task()
    # run_coroutine_task_pool()
    run_coroutine_task_partial()