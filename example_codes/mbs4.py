# -*- encoding:utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__ENTITY_author__ = "SIX DIGIT INVESTMENT GROUP"
__author__ = "GWONGZAN"

import bs4.element
from bs4 import BeautifulSoup
import re
import unicodedata


html_str = """
<html>
	<head>
		<title>Python爬虫开发与项目实战</title>
		<meta charset="UTF-8">
	</head>
	<body>
	Hn标题标记---->>
	<br>
		<h1>Python爬虫</h1>
		<h2>Python爬虫</h2>
		<h3>Python爬虫</h3>
		<h4>Python爬虫</h4>
		<h5>Python爬虫</h5>
		<h6>Python爬虫</h6>
	font标记---->>
	<font size="1">Python爬虫</font>
	<font size="3">Python爬虫</font>
	<font size="7">Python爬虫</font>
	<font size="7" color="red" face="微软雅黑">Python爬虫</font>
	<font size="7" color="red" face="宋体">Python爬虫</font>
	<font size="7" color="red" face="新细明体">Python爬虫</font>
	<br>
	B标记加粗---->>
	<b>Python爬虫</b>
	<br>
	i标记斜体---->>
	<i>Python爬虫</i>
	<br>
	sub下标标记---->>
	2<sub>2</sub>
	<br>
	sup上标标记---->>
	2<sup>2</sup>
	<br>
	引用标记---->>
	<cite>Python爬虫</cite>
	<br>
	em标记表示强调，显示为斜体---->>
	<em>Python爬虫</em>
	<br>
	strong标记表示强调，加粗显示---->>
	<strong>Python爬虫</strong>
	<br>
	small标记，可以显示小一号字体，可以嵌套使用---->>
	<small>Python爬虫</small>
	<small><small>Python爬虫</small></small>
	<small><small><small>Python爬虫</small></small></small>
	<br>
	big标记，显示大一号的字体---->>
	<big>Python爬虫</big>
	<big><big>Python爬虫</big></big>
	<br>
	u标记是显示下划线---->>
	<big><big><big><u>Python爬虫</u></big></big></big>
	<br>
	</body>
</html>

"""

soup = BeautifulSoup(html_str, 'lxml', from_encoding='utf-8')
with open('student.html', encoding='utf-8') as f:
    soup2 = BeautifulSoup(f, 'lxml', from_encoding='utf-8')

# print(soup2.prettify())
# print(unicodedata.unicode(soup.font.string))

if type(soup.font.string) == bs4.element.Comment:
    print(soup.font.string)

# print(soup.body.contents)
#
# for child in soup.body.descendants:
#     print(child)

# for string in soup.stripped_strings:
#     print(string)

print(soup.find_all(re.compile("^b")))
