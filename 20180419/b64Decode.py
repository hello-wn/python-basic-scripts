# -*- coding: utf-8 -*-
import base64

#补全被去掉=的字符串，并进行解码
def safe_base64_decode(s):
    extra = len(s) % 4
    if extra == 0:
        return base64.b64decode(s)
    else:
        for i in range(4 - extra):
            s += b'='
        return base64.b64decode(s)

# test
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('OK') 
