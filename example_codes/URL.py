# -*- encoding:utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__ENTITY_author__ = "SIX DIGIT INVESTMENT GROUP"
__author__ = "GWONGZAN"

# request and response
import requests
from requests.exceptions import HTTPError

"""
请求与响应
headers 处理
cookie 处理
timeout 设置
http 响应码
redirect
proxy
"""

url = 'https://www.zhihu.com/login'
data = {'username': 'qiye', 'password': 'qiye_pass'}
content_type = [
    'application/xml',
    'application/json',
    'application/x-www-form-urlencoded',
]

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
header = {
    'User-Agent': user_agent,
    'Referer': 'https://www.zhihu.com'
}

proxies = {
    'http': '62.33.136.222:8080',
    'https': '35.233.16.212:80',
    'http':'140.83.32.175:80',
    'https':'51.103.137.65:80',
}

try:
    response = requests.get(url=url, data=data, headers=header, timeout=10)  #, proxies=proxies)
    if response.status_code == 400:
        print(response.text)
        print(response.cookies)
    print(response.url == url)
    print(response.request)
    if response.history:
        for resp in response.history:
            print(resp.url)
except HTTPError as e:
    print(f'{e}')




