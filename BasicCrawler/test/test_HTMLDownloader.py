# -*- encoding:utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__ENTITY_author__ = "SIX DIGIT INVESTMENT GROUP"
__author__ = "GWONGZAN"

from BasicCrawler.HTML_Downloader import HTMLDownloader


def test_download():
    content = HTMLDownloader().download('https://en.wikipedia.org/wiki/Pinyin')
    print(content)


if __name__ == "__main__":
    test_download()