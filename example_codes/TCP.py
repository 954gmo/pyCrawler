# -*- encoding:utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__ENTITY_author__ = "SIX DIGIT INVESTMENT GROUP"
__author__ = "GWONGZAN"

# create socket, bind local ip and port
# listen
# loop
# receive and send data
# close socket

import socket
import threading
import time


def handle_client(sock, addr):
    print(f"Accept New connections from {addr}")
    sock.send(b'Hello, I am Server!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        print(f'-->>{data.decode("utf-8")}')
    sock.close()
    print(f'Connection from {addr} closed')


if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 9999))
    s.listen(5)
    print("waiting for connections")
    while True:
        sock, addr = s.accept()
        t = threading.Thread(target=handle_client, args=(sock, addr))
        t.start()

