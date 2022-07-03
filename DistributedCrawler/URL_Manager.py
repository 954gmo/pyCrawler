# -*- encoding:utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__ENTITY_author__ = "SIX DIGIT INVESTMENT GROUP"
__author__ = "GWONGZAN"

import pickle
import hashlib
from sig_logger import console_info, console_err


class URLManager(object):
    def __init__(self):
        self.new_urls = self.load_progress('new_urls.txt')
        self.old_urls = self.load_progress('old_urls.txt')

    def has_new_url(self):
        return self.new_url_size() != 0

    def get_new_url(self):
        new_url = self.new_urls.pop()
        m = hashlib.md5()
        m.update(new_url.encode('utf-8'))
        self.old_urls.add(m.hexdigest()[8:-8])
        return new_url

    def add_new_url(self, url):
        if url is None:
            return
        m = hashlib.md5()
        m.update(url.encode('utf-8'))
        url_md5 = m.hexdigest()[8:-8]
        if (url not in self.new_urls) and (url_md5 not in self.old_urls):
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        if (urls is None) or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def new_url_size(self):
        return len(self.new_urls)

    def old_url_size(self):
        return len(self.old_urls)

    def save_progress(self, path, data):
        with open(path, 'wb') as f:
            pickle.dump(data, f)

    def load_progress(self, path):
        console_info(f'loading progress from file ({path}) ....')
        try:
            with open(path, 'rb') as f:
                tmp = pickle.load(f)
                return tmp
        except Exception as e:
            console_err(f'[!] no progress file, {path}, create new set()')
        return set()