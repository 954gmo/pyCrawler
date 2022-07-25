# -*- encoding:utf-8 -*-
import PyPDF2
from pathlib import Path
import os
import re

if __name__ == "__main__":
    file = os.path.join(Path(__file__).parent, 'sdge_bill.pdf')
    with open(file, 'rb') as pdf_file_obj:
        reader = PyPDF2.PdfFileReader(pdf_file_obj)
        text = ''
        for page in reader.pages:
            text += page.extractText()
    tmp = re.sub(r'\s+', ' ', text)
    tmp = re.search(r"Electric Service.*(Meter Number:.*?)(?P<meter_number>\d+).*Total Taxes & Fees on Electric Charges .*\$(?P<total_tax>\d+\.?\d+).*?Total Electric Service", tmp)
    print(f'Meter Number: {tmp["meter_number"]} \nTotal Taxes & Fees on Electric Charges: -{tmp["total_tax"]}')


