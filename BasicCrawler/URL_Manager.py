# -*- encoding:utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__ENTITY_author__ = "SIX DIGIT INVESTMENT GROUP"
__author__ = "GWONGZAN"


class URLManager:

    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def has_new_url(self):
        """
        determine if there is new url to crawle
        :return:
        """
        return self.new_url_size() != 0

    def add_new_url(self, url):
        """
        add new url to existing URL set
        :param url:
        :return:
        """
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        """
        add new urls to exiting URL set
        :param urls:
        :return:
        """
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def get_new_url(self):
        """
        get a new url
        :return:
        """
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    def new_url_size(self):
        """
        size of new nurl
        :return:
        """
        return len(self.new_urls)

    def old_url_size(self):
        """
        size of old url
        :return:
        """
        return len(self.old_urls)


if __name__ == "__main__":
    import doctest
    import pytest






    test_has_new_url()