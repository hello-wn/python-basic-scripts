# -*- coding: utf-8 -*-
import types, functools
def log(param="exe"):
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kw):
#            print("%s\n"%param)
            print("begin call")
            fn(*args, **kw)
            print("end call")
        return wrapper
    if not isinstance(param, types.FunctionType):
        return decorator
    else:
        return decorator(param)

# 测试
@log('e')
def f():
    print("I am running!")

@log
def b():
    print("I am running too!")

f()
b()
