# -*- encoding:utf-8 -*-
import os
from pathlib import Path
from bs4 import BeautifulSoup
import re


def parse_html(file=''):
    with open(file, 'r', encoding='utf8') as f:
        soup = BeautifulSoup(f, 'html.parser')
    return soup


def html_parser(soup=''):
    res = soup
    return res


if __name__ == "__main__":
    file = os.path.join(Path(__file__).parent, 'tmp.html')
    txt = parse_html(file)
    res = html_parser(txt)
    print(res)
