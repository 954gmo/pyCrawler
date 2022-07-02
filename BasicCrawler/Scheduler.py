# -*- encoding:utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__ENTITY_author__ = "SIX DIGIT INVESTMENT GROUP"
__author__ = "GWONGZAN"


from BasicCrawler.DataStorage import DataOutput
from BasicCrawler.HTML_Downloader import HTMLDownloader
from BasicCrawler.HTMLParser import HtmlParser
from BasicCrawler.URL_Manager import URLManager


class Scheduler(object):
    def __init__(self):
        self.manager = URLManager()
        self.downloader = HTMLDownloader()
        self.parser = HtmlParser()
        self.output = DataOutput()

    def crawl(self, root_url, file):
        self.manager.add_new_url(root_url)
        while self.manager.has_new_url() and (self.manager.old_url_size() < 100):
            try:
                new_url = self.manager.get_new_url()
                html = self.downloader.download(new_url)
                new_urls, data = self.parser.parser(new_url, html)
                self.manager.add_new_urls(new_urls)
                self.output.store_data(data)
                print(f'crawled {self.manager.old_url_size()}')
            except Exception as e:
                print("crawl failed")
                print(e)
        self.output.output_html(file)


if __name__ == "__main__":
    spider_man = Scheduler()
    spider_man.crawl('https://zh.wikipedia.org/wiki/%E8%AF%BA%E8%B4%9D%E5%B0%94%E7%94%9F%E7%90%86%E5%AD%A6%E6%88%96%E5%8C%BB%E5%AD%A6%E5%A5%96%E5%BE%97%E4%B8%BB%E5%88%97%E8%A1%A8', 'chinese_wiki.html')
