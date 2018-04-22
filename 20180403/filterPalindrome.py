# -*- coding: utf-8 -*-
# 我写的这个方法有点蠢，只想到了一半一半的切片，没想到可以完整的倒序匹配
def is_palindrome(n):
    nStr = str(n)
    if len(nStr) == 1:
        return n
    elif len(nStr) % 2 == 0:
        mid = len(nStr) / 2
        if nStr[:mid] == nStr[mid:][::-1]:
            return n
    else:
        mid = len(nStr) / 2
        if nStr[:mid] == nStr[mid + 1:][::-1]:
            return n

output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
