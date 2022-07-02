# -*- encoding:utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__ENTITY_author__ = "SIX DIGIT INVESTMENT GROUP"
__author__ = "GWONGZAN"

import codecs
import time


class DataOutput(object):
    def __init__(self):
        self.data = list()
        self.filepath = ''

    def construct_file_path(self, file):
        self.filepath = f'{file}_{time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())}'

    def store_data(self, data):
        if data is None:
            return
        self.data.append(data)
        if len(self.data) > 10:
            self.output_html(self.filepath)

    def output_head(self, path):
        with open(path, 'w', encoding='utf-8') as fout:
            fout.write('<html>')
            fout.write('<body>')
            fout.write('<table>')

    def output_end(self, path):
        with open(path, 'a', encoding='utf-8') as fout:
            fout.write('</table>')
            fout.write('</body>')
            fout.write('</html>')

    def output_html(self, path):
        with open(path, 'a', encoding='utf-8') as fout:
            for data in self.data:
                fout.write("<tr>")
                fout.write(f"""<td><a href="{data['url']}">{data['url']}</a></td>""")
                fout.write(f""""<td>{data['title']}</td>""")
                fout.write(f"""<td>{data['summary']}</td>""")
                fout.write("</tr>")
                self.data.remove(data)