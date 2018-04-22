# -*- coding: utf-8 -*-
def trim_wn(s):
    start = 0
    for i in s:
        if i.isspace():
            start += 1
            continue
        else:
            break
    end = 0
    for i in s[::-1]:
        if i.isspace():
            end += 1
            continue
        else:
            break
    if end > 0:
        final = s[start:-end]
    else:
        final = s[start:]

    print("final:" + final)
    return final

def trim(s):
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s



# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')





