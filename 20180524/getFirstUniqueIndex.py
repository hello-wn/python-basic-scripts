# -*- coding: utf-8 -*-
# Given a lsit of Integer, find the first non-repeating Integer in it and return it's index. If it donesn't exist, return -1.

class Solution(object):
    def firstUniqueInteger(self, alist): 
        repeatList = []
        i = 0
        while i < len(alist):
            if alist[i] in alist[i+1:]:
                repeatList.append(alist[i])
            elif alist[i] not in repeatList:
                return i
            i += 1
        return -1

solution = Solution()
alist = [43,56,43,56,23,43]
assert solution.firstUniqueInteger([2,4,5,2,4,5,]) == -1
assert solution.firstUniqueInteger([32,342,342,32,34]) == 4 
