# -*- encoding:utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__ENTITY_author__ = "SIX DIGIT INVESTMENT GROUP"
__author__ = "GWONGZAN"

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))
print(f'-->> {s.recv(1024).decode("utf-8")}')
s.send(b'Hello, I am a client')
print(f"--> {s.recv(1024).decode('utf-8')}")
s.send('exit')
s.close()