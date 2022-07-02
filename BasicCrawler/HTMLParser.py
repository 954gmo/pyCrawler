# -*- encoding:utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__ENTITY_author__ = "SIX DIGIT INVESTMENT GROUP"
__author__ = "GWONGZAN"

import re
from urllib.parse import urljoin
from bs4 import BeautifulSoup


class HtmlParser(object):

    def parser(self, page_url, html_cont):
        """
        parse HTML content, extract URL and data
        :param page_url:
        :param html_cont:
        :return:
        """
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)

        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        """
        extract a set of new URLs
        :param page_url:
        :param soup:
        :return:
        """
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r'/wiki/.*'))
        for link in links:
            new_url = link['href']
            new_full_url = urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        """
        extract effective data
        :param page_url:
        :param soup:
        :return:
        """
        data = dict()
        data['url'] = page_url
        title = soup.find('h1', {'id': 'firstHeading'})
        if title:
            data['title'] = title.get_text()
        summary = soup.find('div', {'class': 'shortdescription'})
        if summary:
            data['summary'] = summary.get_text()

        return data





