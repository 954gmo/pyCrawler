# -*- encoding:utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__ENTITY_author__ = "SIX DIGIT INVESTMENT GROUP"
__author__ = "GWONGZAN"

import codecs


class DataOutput(object):

    def __init__(self):
        self.data = list()

    def store_data(self, data):
        if data is None:
            return

        self.data.append(data)

    def output_html(self, file):
        fout = codecs.open(file, 'w', encoding='utf-8')
        fout.write('<html>')
        fout.write('<body>')
        fout.write('<table>')
        for data in self.data:
            fout.write("<tr>")
            fout.write(f"<td>{data['url']}</td>")
            if "title" in data:
                fout.write(f"<td>{data['title']}</td>")
            if "summary" in data:
                fout.write(f"<td>{data['summary']}</td>")
            fout.write("</tr>")
            self.data.remove(data)

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()