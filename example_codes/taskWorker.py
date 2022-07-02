# -*- encoding:utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__ENTITY_author__ = "SIX DIGIT INVESTMENT GROUP"
__author__ = "GWONGZAN"

import time
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass


QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

server_addr = '127.0.0.1'
print(f'Connect to server {server_addr}')

m = QueueManager(address=(server_addr, 8001), authkey=b'qiye')
m.connect()

task = m.get_task_queue()
result = m.get_result_queue()

while (not task.empty()):
    image_url = task.get(True, timeout=5)
    print(f'run task download {image_url}')
    time.sleep(1)
    result.put(f'{image_url} ---> success')

print('worker exit.')