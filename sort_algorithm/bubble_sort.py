# -*- coding: utf-8 -*-

def bubbleSort(alist):
    l = len(alist)
    count = 0
    for i in range(1, l):
        for j in range(0, l-i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
                count += 1
    return alist

alist = [2, 5, 0, 80, 29]
bubbleSort(alist)
print(alist)
