# -*- encoding:utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__ENTITY_author__ = "SIX DIGIT INVESTMENT GROUP"
__author__ = "GWONGZAN"

import os
from pathlib import Path


SERVER = '83.229.5.94'
PORT = 8005
AUTH_KEY = 'sig_baike'.encode('utf-8')
MAX_URL = 2000
WRITE_PER_ENTRY_CNT = 20

BASE_DIR = Path(__file__).resolve().parent
STORAGE = os.path.join(BASE_DIR, 'data')

if not os.path.exists(STORAGE):
    os.makedirs(STORAGE)




