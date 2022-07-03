# -*- encoding:utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__ENTITY_author__ = "SIX DIGIT INVESTMENT GROUP"
__author__ = "GWONGZAN"

from multiprocessing.managers import BaseManager
import time
from multiprocessing import Process, Queue

from URL_Manager import URLManager
from DataStorage import DataOutput
import settings
from sig_logger import info_logger, debug_logger, err_logger, console, console_info


class Scheduler(object):
    @staticmethod
    def start_scheduler(url_q, result_q):
        """
        start a distributed scheduler
        :param url_q: for URL_manager_proc() to pass URL to worker nodes
        :param result_q: for worker nodes to return data to result_solve_proc()
        :return: instance of a multiprocessing manager
        """

        console_info("registering task queue ... ")
        BaseManager.register('get_task_queue', callable=lambda: url_q)

        console_info("registering result queue ...")
        BaseManager.register('get_result_queue', callable=lambda: result_q)

        console_info("starting Scheduler ...")
        scheduler = BaseManager(address=('', settings.PORT), authkey=settings.AUTH_KEY)
        console_info("Scheduler Started")

        return scheduler

    @staticmethod
    def url_manager_proc(url_q, conn_q, root_url):
        """

        :param url_q: for URL_manager_proc() to pass URL to worker nodes
        :param conn_q: new URL passed to url_manager_proc() from result_solve_proc()
        :param root_url: seed url
        :return:
        """
        console_info("starting URL manager process ... ")

        url_manager = URLManager()
        url_manager.add_new_url(root_url)

        while True:
            while url_manager.has_new_url():
                new_url = url_manager.get_new_url()
                url_q.put(new_url)
                console_info(f"url_q  approximate size: {url_q.qsize()}, new url added to url_q: {new_url}")
                console_info(f"old_url_size={url_manager.old_url_size()}")

                if url_manager.old_url_size() > settings.MAX_URL:
                    console_info(f"crawled {settings.MAX_URL} urls, should end the task")
                    url_q.put('end')
                    console_info('Scheduler Notify finishing task')

                    url_manager.save_progress('new_urls.txt', url_manager.new_urls)
                    url_manager.save_progress('old_urls.txt', url_manager.old_urls)

                    console.info("progress saved to new_urls.txt and old_urls.txt")
                    return

            try:
                urls = conn_q.get()
                console_info(f"new urls {urls}")
                url_manager.add_new_urls(urls)
            except BaseException as e:
                time.sleep(0.1)

    @staticmethod
    def result_solve_proc(result_q, conn_q, store_q):
        """

        :param result_q: returned data to result_solve_proc() from worker Nodes
        :param conn_q: new URLs to be passed to url_manager_proc()
        :param store_q: data to be passed to store_proc()
        :return:
        """
        while True:
            try:
                if not result_q.empty():
                    content = result_q.get(True)
                    if content['new_urls'] == 'end':
                        console_info("Scheduler Notified to Stop working")
                        store_q.put('end')
                        return
                    conn_q.put(content['new_urls'])
                    store_q.put(content['data'])
                else:
                    time.sleep(0.1)
            except BaseException as e:
                time.sleep(0.1)

    @staticmethod
    def store_proc(store_q):
        """

        :param store_q: data from result_solve_proc()
        :return:
        """
        output = DataOutput()
        output.construct_file_path('wikipedia')
        while True:
            if not store_q.empty():
                data = store_q.get()
                if data == 'end':
                    console_info(f"Signal fired to End the Task, save result to {output.filepath}")
                    output.output_end(output.filepath)
                    return
                console_info(f"store data")
                output.store_data(data)


if __name__ == '__main__':
    url_q = Queue()     # for url_manager_proc() to pass URL to worker Nodes
    result_q = Queue()  # for worker nodes to return data to result_solve_proc()
    store_q = Queue()   # for result_solve_proc() to pass data to store_proc()
    conn_q = Queue()    # for result_solve_proc() to pass new URL to url_manager_proc()

    manager = Scheduler.start_scheduler(url_q, result_q)
    url_manager_proc = Process(target=Scheduler.url_manager_proc, args=(url_q, conn_q, 'https://en.wikipedia.org/wiki/Port_(computer_networking)', ))
    result_solve_proc = Process(target=Scheduler.result_solve_proc, args=(result_q, conn_q, store_q, ))
    store_proc = Process(target=Scheduler.store_proc, args=(store_q, ))

    url_manager_proc.start()
    result_solve_proc.start()
    store_proc.start()

    url_manager_proc.join()
    result_solve_proc.join()
    store_proc.join()

    manager.get_server().serve_forever()