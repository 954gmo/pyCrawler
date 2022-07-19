# -*- encoding:utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__ENTITY_author__ = "SIX DIGIT INVESTMENT GROUP"
__author__ = "GWONGZAN"

import PyPDF2

file_obj = '../UtilityAPI/PembrokePinesFL UB Bill PDF.pdf'
pdf_file_obj = open(file_obj, 'rb')
reader = PyPDF2.PdfFileReader(pdf_file_obj)
# reader.decrypt('')
page = reader.getPage(0)
contents = page.getContents()
# print(page.extract_text())
# print(reader.getDocumentInfo())
print(page.extractText())




import os
from pathlib import Path
import keyboard
import time
import re

from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import HTMLConverter, TextConverter
from pdfminer.cmapdb import CMapDB
from pdfminer.layout import LAParams


def create_txt_files_using_adobe(path, filename, t=2):
    ESC = 'esc'
    read_path = Path(str(os.path.join(path, filename)))
    write_path = Path(str(os.path.join(read_path.parent, read_path.stem)) + ".txt")
    overwrite_file = os.path.exists(write_path)

    os.startfile(read_path)
    time.sleep(t)
    keyboard.press_and_release('alt')
    time.sleep(t)
    keyboard.press_and_release('f') # open file menu
    time.sleep(t)
    keyboard.press_and_release('v') # select "save as text" option
    time.sleep(t)
    keyboard.write(str(write_path))
    time.sleep(t)
    keyboard.press_and_release('alt+s')
    time.sleep(t)
    if overwrite_file:
        keyboard.press_and_release('y')
    time.sleep(t)
    keyboard.press_and_release('ctrl+w')
    return


def pdf_2_txt(infile, outfile, outtype='txt'):
    debug = 0
    pagenos = set()
    caching = True
    imagewriter = None
    laparams = LAParams()
    rotation = 0
    maxpages = 0
    scale = 1
    layoutmode = 'normal'

    PDFDocument.debug = debug
    PDFParser.debug = debug
    CMapDB.debug = debug
    PDFPageInterpreter.debug = debug

    rsrcmgr = PDFResourceManager(caching=caching)

    with open(outfile, 'w', encoding='utf-8') as outfp,  \
            open(infile, 'rb') as infp:
        if outtype == 'txt':
            device = TextConverter(rsrcmgr, outfp, laparams=laparams,
                               imagewriter=imagewriter)
        elif outtype == 'html':
            device = HTMLConverter(rsrcmgr, outfp, scale=scale,
                                   layoutmode=layoutmode, laparams=laparams,
                                   imagewriter=imagewriter, debug=debug)

        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.get_pages(infp, pagenos, maxpages=maxpages,
                                      caching=caching, check_extractable=True):
            page.rotate = (page.rotate+rotation) % 360
            interpreter.process_page(page)
        device.close()

    return


def parse_pdf_txt(file):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        print(content)

if __name__ == "__main__":
    folder = Path(__file__).parent
    out_file = os.path.join(folder, 'pdf2txt_output.txt')
    in_file = os.path.join(folder, '../UtilityAPI/PembrokePinesFL UB Bill PDF.pdf')
    # create_txt_files_using_adobe(os.getcwd(), '.pdf')
    # pdf_2_txt(in_file, out_file, outtype='html')
    pdf_2_txt(in_file, out_file)
    parse_pdf_txt(out_file)