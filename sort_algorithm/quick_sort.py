# -*- coding: utf-8 -*-
def quickSort(alist, left, right):
    if(left < right):
        midkey = alist[left]
        i, j = left, right
        while(i < j):
            #从最后一个元素开始寻找，比中间值小的值
            while(i < j and alist[j] > midkey):
                j -= 1
            alist[i] = alist[j]
            #从第一个元素开始寻找，比中间值大的值
            while(i < j and alist[i] < midkey):
                i += 1
            alist[j] = alist[i]
        alist[i] = midkey
        quickSort(alist, left, i-1)
        quickSort(alist, i+1, right)

alist = [9, 3, 11, 5, 7, 32, 1]
quickSort(alist, 0, len(alist)-1)
print(alist)
