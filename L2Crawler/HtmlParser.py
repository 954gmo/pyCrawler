# -*- encoding:utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__ENTITY_author__ = "SIX DIGIT INVESTMENT GROUP"
__author__ = "GWONGZAN"

import json
import re

from HtmlDownloader import HtmlDownloader


class HtmlParser(object):

    def parser_url(self, page_url, response):
        pattern = re.compile(r'')
        urls = pattern.findall(response)

        if urls is not None:
            return list(set(urls))
        else:
            return None

    def parser_json(self, page_url, response):
        pattern = re.compile(r'')
        result = pattern.findall(response)[0]

        if result is not None:
            value = json.loads(result)
            try:
                is