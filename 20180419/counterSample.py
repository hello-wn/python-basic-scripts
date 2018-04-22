# -*- coding: utf-8 -*-
from collections import Counter

c = Counter()
for char in 'testcharisme':
    c[char] += 1

print(c)
# Counter({'s': 2, 'e': 2, 't': 2, 'r': 1, 'i': 1, 'm': 1, 'a': 1, 'h': 1, 'c': 1})
