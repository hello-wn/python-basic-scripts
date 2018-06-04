# -*- coding: utf-8 -*-
def selectSort(alist):
    l = len(alist)
    for i in range(0, l-1):
        min_index = i
        for j in range(i+1, l):
            if alist[j] < alist[min_index]:
                min_index = j
        if i != min_index:
            alist[i], alist[min_index] = alist[min_index], alist[i]
    return alist

alist = [9, 3, 1, 4, 99, 23, 4]
print(selectSort(alist))
    
