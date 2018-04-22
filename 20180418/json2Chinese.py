# -*- coding: utf-8 -*-
import json

obj = dict(name = '小明', age = 20)
s1 = json.dumps(obj, ensure_ascii = True)
s2 = json.dumps(obj, ensure_ascii = False)

print(s1)   #{"name": "\u5c0f\u660e", "age": 20}
print(s2)   #{"name": "小明", "age": 20}
