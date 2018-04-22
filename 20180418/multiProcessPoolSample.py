# -*- coding: utf-8 -*-
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task: %s, pid: %s' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process pid: %s' % os.getpid())
    # 设置最多同时执行4个进行
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args = (i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')


# Parent process pid: 1976
# Waiting for all subprocesses done...
# Run task: 0, pid: 1977
# Run task: 1, pid: 1979
# Run task: 2, pid: 1980
# Run task: 3, pid: 1978
# Task 2 runs 0.59 seconds.
# Run task: 4, pid: 1980
# Task 0 runs 1.03 seconds.
# Task 3 runs 1.82 seconds.
# Task 1 runs 2.78 seconds.
# Task 4 runs 2.81 seconds.
# All subprocesses done.
