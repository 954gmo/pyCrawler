# -*- encoding:utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__ENTITY_author__ = "SIX DIGIT INVESTMENT GROUP"
__author__ = "GWONGZAN"

import os

from bs4 import BeautifulSoup
from pathlib import Path
import requests


def example():
    url = "https://www.tutorialspoint.com/index.htm"
    webpage_response = requests.get(url)
    webpage = webpage_response.content

    soup = BeautifulSoup(webpage, 'html.parser')
    title_tag = soup.title
    name_title_tag = title_tag.name
    title_tag.name = 'new name'
    title.attrs


def example2():
    html_doc = """
    <html><head><title>Tutorials Point</title></head>
    <body>
    <p class="title"><b>The Biggest Online Tutorials Library, It's all Free</b></p>
    <p class="prog">Top 5 most used Programming Languages are:
    <a href="https://www.tutorialspoint.com/java/java_overview.htm" class="prog" id="link1">Java</a>,
    <a href="https://www.tutorialspoint.com/cprogramming/index.htm" class="prog" id="link2">C</a>,
    <a href="https://www.tutorialspoint.com/python/index.htm" class="prog" id="link3">Python</a>,
    <a href="https://www.tutorialspoint.com/javascript/javascript_overview.htm" class="prog" id="link4">JavaScript</a> and
    <a href="https://www.tutorialspoint.com/ruby/index.htm" class="prog" id="link5">C</a>;
    as per online survey.</p>
    <p class="prog">Programming Languages</p>
    """
    soup = BeautifulSoup(html_doc, 'html.parser')
    title = soup.title.string
    print(title)



def sample():

    url = "https://www.tutorialspoint.com/index.htm"
    webpage_response = requests.get(url)
    webpage = webpage_response.content

    # create a beautifulSoup objects from a webpage
    soup = BeautifulSoup(webpage, 'html.parser')
    print(soup.title)
    for link in soup.find_all('a'):
        print(link.get('href'))

    basedir = Path(__file__).parent
    webpage_html = "ref.html"
    file = os.path.join(basedir, webpage_html)

    with open(file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')


    # within the `soup` object, tags can be called by name
    title = soup.title
    # or by CSS selector
    all_elem_of_header_class = soup.select(".header")
    # or by a call to `.find_all`:
    all_p_elem = soup.find_all('p')

if __name__ == "__main__":
    example2()



