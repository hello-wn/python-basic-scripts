# -*- coding: utf-8 -*-

# 列表去重的多种方法
l1 = ['a', 'c', 'b', 'a', 4, 3, 4]

# 用集合
l2 = list(set(l1))
# print(l2)

# 用字典
l3 = list({}.fromkeys(l1).keys())
# print(l3)

# set + 保持顺序
l4 = list(set(l1))
l4.sort(key=l1.index)
# print(l4)

# 列表推导式
l5 = []
[l5.append(i) for i in l1 if not i in l5]
print(l5)
