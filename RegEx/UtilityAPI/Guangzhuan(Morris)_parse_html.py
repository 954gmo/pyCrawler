# -*- encoding:utf-8 -*-
import os
from pathlib import Path
from bs4 import BeautifulSoup
import re

def parse_html(file=''):
    base_dir = Path(__file__).parent
    file = os.path.join(base_dir, file)

    with open(file, 'r', encoding='utf8') as f:
        soup = BeautifulSoup(f, 'html.parser')


if __name__ == "__main__":
    parse_html('')