# -*- encoding:utf-8 -*-
import PyPDF2
from pathlib import Path
import os
import re


def read_pdf_txt(file=''):
    with open(file, 'rb') as pdf_file_obj:
        reader = PyPDF2.PdfFileReader(pdf_file_obj)
        text = ''
        for page in reader.pages:
            text += page.extractText()
    return txt


def pdf_parser(content=''):
    return res


if __name__ == "__main__":
    txt = read_pdf_txt(file=os.path.join(Path(__file__).parent, ''))
    res = pdf_parser(txt)
    print(res)