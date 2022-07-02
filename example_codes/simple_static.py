# -*- encoding:utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__ENTITY_author__ = "SIX DIGIT INVESTMENT GROUP"
__author__ = "GWONGZAN"

import requests
from bs4 import BeautifulSoup
import json
import csv
from collections import namedtuple


user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
header = {
    'User-Agent': user_agent,
}
url = 'http://www.daomubiji.org/'

r = requests.get(url, headers=header)
print(r.encoding)
r.encoding = r.apparent_encoding
content = []


soup = BeautifulSoup(r.text, 'lxml', from_encoding='utf-8')
for panel in soup.find_all(class_="panel"):
    h2 = panel.find('h2')

    if h2 is not None:
        h2_title = h2.string
        l = []
        for a in panel.find_all('a'):
            href = a.get('href')
            l.append({'href': href, 'box_title': a.string})
        content.append({'title': h2_title, 'content': l})
with open("daomubiji.json", 'w') as fp:
    json.dump(content, fp=fp, indent=4)

# import requests
#
# url = "http://search.51job.com"
# res = requests.get(url)
# res.encoding = "gbk"
# html = res.text
# print(html)

# import requests
#
# url = "http://search.51job.com"
# res = requests.get(url)
# res.encoding = res.apparent_encoding
# html = res.text
# print(html)


# import requests
#
# url = "http://search.51job.com"
# res = requests.get(url)
# html = res.text.encode('iso-8859-1').decode('gbk')
# print(html)
#
# 作者：菜鸟分析
# 链接：https://www.zhihu.com/question/39432369/answer/573223907
# 来源：知乎
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

headers = ['ID', 'UserName', 'Password', 'Age', 'Country']
rows = [
    (1001, 'qiye', 'qiye_pass', 24, 'China'),
    (1002, 'Mary', 'Mary_pass', 25, 'USA'),
    (1003, 'Jack', "Jack_pass", 20, "USA"),
]

with open('qiye.csv', 'w', newline='', encoding='utf-8') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)

rows_2 = [
    {'ID': 1001, 'UserName': "qiye", "Password": "qiye_pass", 'Age': 24, 'Country': 'China'},
    {'ID': 1003, 'UserName': "Jack", 'Password': "Jack_pass", "Age": 20, 'Country': "USA"},
    {"ID": 1002, "UserName": "Mary", "Password": "Mary_pass", "Age": 20, 'Country': "USA"},
]

with open('qiye_1.csv', 'w') as f:
    f2_csv = csv.DictWriter(f, headers)
    f2_csv.writeheader()
    f2_csv.writerows(rows_2)

with open('qiye.csv') as f:
    f_csv = csv.reader(f)
    headings = next(f_csv)
    # print(str(headings))
    Row = namedtuple('Row', headings)
    for r in f_csv:
        if r:
            row = Row(*r)
            print(row.UserName, row.Password)
            print(row)

