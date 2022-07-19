# -*- encoding:utf-8 -*-
import PyPDF2
from pathlib import Path
import os


def parse_pdf(file=''):
    with open(file, 'rb') as pdf_file_obj:
        reader = PyPDF2.PdfFileReader(pdf_file_obj)
        # # reader.decrypt('')
        # page = reader.getPage(0)
        # contents = page.getContents()
        # print(page.extract_text())
        text = ''
        for page in reader.pages:
            text += page.extractText()
        print(text)


if __name__ == "__main__":
    parse_pdf(file=os.path.join(Path(__file__).parent, 'PembrokePinesFL UB Bill PDF.pdf'))