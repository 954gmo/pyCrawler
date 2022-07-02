# -*- encoding:utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__ENTITY_author__ = "SIX DIGIT INVESTMENT GROUP"
__author__ = "GWONGZAN"

from BasicCrawler.URL_Manager import URLManager


def test_has_new_url():
    url_manager = URLManager()
    assert url_manager.has_new_url() == False
    url_manager.add_new_url('new_url')
    assert url_manager.has_new_url() == True

def test_add_new_urls():
    url_manager = URLManager()
    url_manager.add_new_urls(['url1', 'url2'])
    assert 2 == url_manager.new_url_size()


if __name__ == "__main__":
    test_has_new_url()
    test_add_new_urls()