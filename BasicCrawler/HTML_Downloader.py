# -*- encoding:utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__ENTITY_author__ = "SIX DIGIT INVESTMENT GROUP"
__author__ = "GWONGZAN"

import requests


class HTMLDownloader(object):

    def __init__(self):
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
        self.headers = {
            'User-Agent': self.user_agent,
        }

    def download(self, url):
        if url is None:
            return None
        r = requests.get(url, headers=self.headers)
        if r.status_code == 200:
            r.encoding = 'utf-8'
            return r.text
        return None

