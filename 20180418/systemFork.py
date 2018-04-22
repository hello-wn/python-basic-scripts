# -*- coding: utf-8 -*-
import os

print('Process (%s) start...\n' % os.getpid())

pid = os.fork()
if pid == 0:
    print('child process pid: %s, parent process pid: %s' % (os.getpid(), os.getppid()))
    print('fork return code: %s\n' % pid)
else:
    print('My pid: %s, my child process pid: %s' % (os.getpid(), pid))
    print('fork return code: %s\n' % pid)

#result:
#Process (17823) start...

# My pid: 17823, my child process pid: 17824
# fork return code: 17824

# child process pid: 17824, parent process pid: 17823
# fork return code: 0


