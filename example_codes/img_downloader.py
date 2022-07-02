# -*- encoding:utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__ENTITY_author__ = "SIX DIGIT INVESTMENT GROUP"
__author__ = "GWONGZAN"

import urllib
import requests
from bs4 import BeautifulSoup

def schedule(block_num, block_size, total_size):
    """

    :param block_num:
    :param block_size:
    :param total_size:
    :return:
    """
    per = 100.0 * block_num * block_size /total_size
    if per > 100:
        per = 100
    print(f'{per}%')


user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 ' \
             'Safari/537.36 '
header = {
    'authority': 'pixabay.com',
    'method': 'GET',
    'path': '/zh/images/search/%E8%8A%B1/',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': '_ga=GA1.2.1134749242.1656027073; _gid=GA1.2.1397063739.1656027073; _hjFirstSeen=1; _hjSession_920442=eyJpZCI6IjlkYjBlZDgwLTFmMTMtNDc1YS1hYTkyLWFlOTM4MDBhY2E5MiIsImNyZWF0ZWQiOjE2NTYwMjcwNzMyOTEsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; is_human=1; csrftoken=m6k3OIWYweXsQdbCgvVktmaVpB4e9ZGDtRJ8pwCbNaACM80aPmkCIk5CnnOyQp6H; lang=zh; anonymous_user_id=236edd4821d741b6be4f881205abd7de; _hjSessionUser_920442=eyJpZCI6IjFkM2MyNzM0LWEwMTItNWVhYi05NmU3LTZlZDYxZTFiMDRkNCIsImNyZWF0ZWQiOjE2NTYwMjcwNzMxNzEsImV4aXN0aW5nIjp0cnVlfQ==; client_width=1903; _hjIncludedInSessionSample=0; dwf_show_canva_ad_in_attribution=False; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Jun+23+2022+20%3A00%3A47+GMT-0400+(Eastern+Daylight+Time)&version=6.31.0&isIABGlobal=false&hosts=&consentId=cd852497-0108-4baa-9a38-0c55d02ff5ba&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false; __cf_bm=Dx43f3UmeZd64YkP5heQns4zfNh.gW5cIJdw_LYHK.Q-1656029129-0-AZxh+eLGtM7pW+NTSy9rEwAnSV7XGcv+LwQpz9zZRs9MKnyWReMbCLZMQkTd5zqJ9+JhOxOEQ73mtsgmHaUXBlQ=',
    'referer': 'https://pixabay.com/zh/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
}
url = 'https://pixabay.com/zh/images/search/%E8%8A%B1/'

r = requests.get(url, headers=header)
r.encoding = r.apparent_encoding
print(r.text)
soup = BeautifulSoup(r.text, 'lxml', from_encoding='utf-8')

img_urls = soup.find_all('img')
for img_url in img_urls:
    print(img_url)