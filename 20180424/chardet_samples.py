# -*- coding: utf-8 -*-
import chardet

print(chardet.detect(b'Hhahahahahaha???'))

data = '你是谁，我是谁'.encode('gbk')
print(chardet.detect(data))

data = '你是谁，我是谁'.encode('utf-8')
print(chardet.detect(data))

# {'encoding': 'ascii', 'confidence': 1.0}
# {'encoding': 'GB2312', 'confidence': 0.99}
# {'encoding': 'utf-8', 'confidence': 0.99}

