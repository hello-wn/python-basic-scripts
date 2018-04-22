# -*- coding: utf-8 -*-
from multiprocessing import Process
import os

def run_proc(name):
    print('Run child process: %s ,pid: %s' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process pid: %s' % os.getpid())
    p = Process(target = run_proc, args = ('test',))
    print('Child process will start.')
    p.start()
    #join方法：等待子进程结束后向下执行
    p.join()
    print('Child process end.')
