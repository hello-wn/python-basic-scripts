# -*- coding: utf-8 -*-
def insertSort(alist):
    l = len(alist)
    for i in range(1, l):
        if(alist[i-1] > alist[i]):
            j, tmp = i, alist[i]
            while(j > 0 and alist[j-1] > tmp):
                #将数值较大的元素后移
                alist[j] = alist[j-1]
                j -= 1
            alist[j] = tmp

        
alist = [9, 3, 11, 5, 7, 32, 1]
insertSort(alist)
print(alist)
