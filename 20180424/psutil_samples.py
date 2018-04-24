# -*- coding: utf-8 -*-

# prepare:
# sudo apt-get install python3-dev
# sudo pip install psutil

import psutil

#print(psutil.cpu_count())

#print(psutil.cpu_count(logical=False))

#print(psutil.cpu_times())

#类似top，每秒刷新一次CPU使用率
#for x in range(10):
#    print(psutil.cpu_percent(interval=1, percpu=True))

#print(psutil.disk_usage('/home/wn'))

#print(psutil.net_if_addrs())

#类似ps aux
print(psutil.test())
