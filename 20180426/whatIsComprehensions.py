# -*- coding: utf-8 -*-

def double(x):
    return x * x

# list推导式
list_res = [double(i) for i in range(10) if i % 2 == 0]
print(list_res)

# use () change to generator
generator_res = (double(i) for i in range(10) if i % 2 == 0)
print(type(generator_res))
for x in generator_res:
    print(x)

# dict推导式
dict_origin = {'a': -2, 'b': 9, 'c': -5}
dict_res = {k.upper(): abs(v) for k, v in dict_origin.items()}
print(dict_res)
# Output: {'B': 9, 'A': 2, 'C': 5}

# 大小写key合并
mcase = {'a': 2, 'b': 23, 'A': 9, 'z': 10}
dict_ress = {
    k.upper(): mcase.get(k.upper(), 0) + mcase.get(k.lower(), 0)
    for k in mcase.keys()
#    if k.lower() in ['a', 'b']
}
print(dict_ress)
# Output: {'A': 11, 'B': 23, 'Z': 10}

# set推导式
squared = {x**2 for x in [1, 1, 2]}
print(squared)
# Output: {1, 4}
