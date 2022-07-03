# -*- encoding:utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__ENTITY_author__ = "SIX DIGIT INVESTMENT GROUP"
__author__ = "GWONGZAN"

import os
import time
import settings
from sig_logger import console_info


class DataOutput(object):
    def __init__(self, file):
        self.data = list()
        self.filepath = f'{file}_{time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())}.html'
        self.filepath = os.path.join(settings.STORAGE, self.filepath)
        self.output_head(self.filepath)

    def store_data(self, data):
        if data is None:
            return
        self.data.append(data)
        if len(self.data) > settings.WRITE_PER_ENTRY_CNT:
            console_info(f"write data to file per {settings.WRITE_PER_ENTRY_CNT} entries")
            self.output_html(self.filepath)

    def output_head(self, path):
        with open(path, 'w', encoding='utf-8') as fout:
            fout.write('<html>')
            fout.write(r'''<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />''')
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
                if 'title' in data:
                    fout.write(f""""<td>{data['title']}</td>""")
                if "summary" in data:
                    fout.write(f"""<td>{data['summary']}</td>""")
                fout.write("</tr>")
                self.data.remove(data)
