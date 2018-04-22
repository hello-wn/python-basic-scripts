# -*- coding: utf-8 -*-
import time, sys, queue
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass

QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

server_addr = '127.0.0.1'
print('Connect to server %s...' % server_addr)
#端口和验证码要与task_master.py设置的一致
m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
#从网络连接
m.connect()
#获取Queue
task = m.get_task_queue()
result = m.get_result_queue()

for i in range(10):
    try:
        #从Queue中获取任务
        n = task.get(timeout=1)
        print('run task %d * %d...' % (n, n))
        r = '%d * %d = %d' % (n, n, n * n)
        time.sleep(1)
        #把结果写入Queue中
        result.put(r)
    except Queue.Empty:
        print('task queue is empty.')

print('worker exit.')
    
