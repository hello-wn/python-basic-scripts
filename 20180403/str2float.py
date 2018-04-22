from __future__ import division
from functools import reduce
digits = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6}
def char2num(s):
    return digits[s];    

def str2float(str):
    parts = str.split('.')
    a = reduce(lambda x,y: x * 10 + y, map(char2num, parts[0]))
    b = reduce(lambda x,y: x * 10 + y, map(char2num, parts[1])) / 10 ** len(parts[1])
    return a + b

print(str2float("123.456"))
