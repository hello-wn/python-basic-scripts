# -*- coding: utf-8 -*-

# 杨氏矩阵查找
# 在一个m行n列二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

def findValue(l, num):
    m = len(l) - 1
    n = len(l[0]) - 1
    i,j = 0, n
    count = 0
    while i <= m and j > 0:
        ele = l[i][j]
        if ele == num:
            print(count)
            return True
        elif ele > num:
            n -= 1
        else:
            i += 1
        count += 1
    print(count)
    return False

list1 = [[1,2,3], [2,3,4],[3,4,5]]
print(findValue(list1, 9))
