# -*- coding: utf-8 -*-
import random, time, queue
from multiprocessing.managers import BaseManager

task_queue = queue.Queue()
result_queue = queue.Queue()

class QueueManager(BaseManager):
    pass

#把两个Queue都注册到网上，callable关联Queue对象
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)
#绑定端口，设置验证码给任务进程验证
manager = QueueManager(address=('', 5000), authkey=b'abc')
#启动Queue
manager.start()

task = manager.get_task_queue()
result = manager.get_result_queue()

for i in range(10):
    n = random.randint(0, 10000)
    print('Put task %d...' % n)
    task.put(n)

print('Try to get results...')
for i in range(10):
    r = result.get(timeout=10)
    print('Result: %s' % r)

manager.shutdown()
print('master.exit.')
