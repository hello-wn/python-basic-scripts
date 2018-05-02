# -*- coding: utf-8 -*-
#with open('test.txt', 'wb') as f:
#    f.write("\x5F\x9D\x3E".encode('utf-8'))

with open('test.txt', 'rb') as f:
    print(f.read().decode('utf-8'))

