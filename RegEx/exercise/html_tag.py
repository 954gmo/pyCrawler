# -*- encoding:utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__ENTITY_author__ = "SIX DIGIT INVESTMENT GROUP"
__author__ = "GWONGZAN"

import re


def html_tags():
    open_tag = r'<[^/>][^>]*>'
    close_tag = r'</[^>]+>'
    self_close = r'<[^/>]+/>'
    all_tag = r'<[^>]+>'
    tags = [open_tag, close_tag, self_close, all_tag]
    txts = ['<table>', '<a href="#label">', '<img src="/img">', '</table>', '<br />', ]
    for tag in tags:
        print(tag)
        for txt in txts:
            print(re.search(tag, txt))


def split_all_str():
    src = 'split all string'
    print(re.findall(r'[\w]', src))
    print(re.findall(r'\w+', src))
    print(re.findall(r'\w', src))
    print(re.findall(r'[\w]+', src))


def split_html():
    import requests
    url = 'https://www.w3resource.com'
    res = requests.get(url)
    html = res.text
    print('open tags')
    print(re.findall(r'<[^/>][^>]+>', html))


def group_comparison():
    mon = re.search(r'(\d{4})-(\d{2})-(\d{2})', '2018-09-01')
    print(mon)
    print(mon.groups())
    for i in range(len(mon.groups()) + 1):
        print(i)
        print(mon.group(i))


def example():
    text = "Birds are beautiful"
    regex = re.compile('(?P<animal>\w+)(?P<verb>\w+)(?P<adjective>\w+)')
    matched = re.search(regex, text)
    print(matched.groups())


if __name__ == "__main__":
    example()
