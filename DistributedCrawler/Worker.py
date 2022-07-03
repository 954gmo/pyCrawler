# -*- encoding:utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__ENTITY_author__ = "SIX DIGIT INVESTMENT GROUP"
__author__ = "GWONGZAN"


from multiprocessing.managers import BaseManager
from HTML_Downloader import HtmlDownloader
from HTML_Parser import HtmlParser
import settings
from sig_logger import console_info, console_err


class Worker(object):
    def __init__(self):
        BaseManager.register('get_task_queue')
        BaseManager.register('get_result_queue')

        console_info(f'connect to server {settings.SERVER}')
        self.m = BaseManager(address=(settings.SERVER, settings.PORT), authkey=settings.AUTH_KEY)
        self.m.connect()

        self.task = self.m.get_task_queue()
        self.result = self.m.get_result_queue()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        console_info('finished initialization')

    def crawl(self):
        while True:
            try:
                if not self.task.empty():
                    url = self.task.get()
                    if url == 'end':
                        console_info("Scheduler Notified to End task")
                        self.result.put({'new_urls': 'end', 'data': 'end'})
                        return
                    console_info(f"Worker is parsing {url.encode('utf-8')}")
                    content = self.downloader.download(url)
                    new_urls, data = self.parser.parser(url, content)
                    self.result.put({"new_urls": new_urls, "data": data})

            except EOFError as e:
                console_err("failed to connect worker node")
                return
            except Exception as e:
                console_err(e)
                console_err('crawl failed')


if __name__ == "__main__":
    worker = Worker()
    worker.crawl()
