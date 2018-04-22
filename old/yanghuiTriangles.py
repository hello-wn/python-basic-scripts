# -*- coding: utf-8 -*-

def triangles():
    L = [1]
    count = 1
    while count < 10:
        yield L
        L.append(0)
        L = [L[i-1] + L[i] for i in range(len(L))]
        count +=1

for L in triangles():
    print(L)
