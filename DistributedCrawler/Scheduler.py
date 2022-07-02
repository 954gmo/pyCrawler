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



class Scheduler(object):
    def start_scheduler(self, url_q, result_q):
        """
        start a distributed scheduler
        :param url_q:
        :param result_q:
        :return:
        """
        BaseManager.register('get_task_queue', callable=lambda: url_q)
        BaseManager.register('get_result_queue', callable=lambda: result_q)
        scheduler = BaseManager(address=('', settings.PORT), authkey=settings.AUTH_KEY)
        return scheduler

    def url_manger_proc(self, url_q, conn_q, root_url):
        url_manager = URLManager()
        url_manager.add_new_url(root_url)
        while True:
            while url_manager.has_new_url():
                new_url = url_manager.get_new_url()
                url_q.put(new_url)
                print(f"old_url={url_manager.old_url_size()}")
                if url_manager.old_url_size() > 2000:
                    url_q.put('end')
                    print('Scheduler Notify finishing task')
                    url_manager.save_progress('new_urls.txt', url_manager.new_urls)
                    url_manager.save_progress('old_urls.txt', url_manager.old_urls)
                    return

            try:
                urls = conn_q.get()
                url_manager.add_new_urls(urls)
            except BaseException as e:
                time.sleep(0.1)

    def result_solve_proc(self, result_q, conn_q, store_q):
        while True:
            try:
                if not result_q.empty():
                    content = result_q.get(True)
                    if content['new_urls'] == 'end':
                        print('Notified Finishing Task')
                        store_q.put('end')
                        return
                    conn_q.put(content['new_urls'])
                    store_q.put(content['data'])
                else:
                    time.sleep(0.1)
            except BaseException as e:
                time.sleep(0.1)

    def store_proc(self, store_q):
        output = DataOutput()
        output.construct_file_path('wikipedia')
        while True:
            if not store_q.empty():
                data = store_q.get()
                if data == 'end':
                    print("ending storage process..")
                    output.output_end(output.filepath)
                    return
                output.store_data(data)


if __name__ == '__main__':
    url_q = Queue()
    result_q = Queue()
    store_q = Queue()
    conn_q = Queue()

    schedule_node = Scheduler()
    manager = schedule_node.start_scheduler(url_q, result_q)
    url_manager_proc = Process(target=schedule_node.url_manger_proc, args=(url_q, conn_q, 'https://en.wikipedia.org/wiki/Port_(computer_networking)', ))
    result_solve_proc = Process(target=schedule_node.result_solve_proc, args=(result_q, conn_q, store_q, ))
    store_proc = Process(target=schedule_node.store_proc, args=(store_q, ))

    url_manager_proc.start()
    result_solve_proc.start()
    store_proc.start()

    manager.get_server().serve_forever()