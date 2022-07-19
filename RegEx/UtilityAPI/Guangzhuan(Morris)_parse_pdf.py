# -*- encoding:utf-8 -*-
import PyPDF2
from pathlib import Path
import os


def read_pdf_txt(file=''):
    with open(file, 'rb') as pdf_file_obj:
        reader = PyPDF2.PdfFileReader(pdf_file_obj)
        text = ''
        for page in reader.pages:
            text += page.extractText()
    return txt


def pdf_parser(content=''):
    pass


if __name__ == "__main__":
    txt = read_pdf_txt(file=os.path.join(Path(__file__).parent, 'PembrokePinesFL UB Bill PDF.pdf'))
    pdf_parser(txt)