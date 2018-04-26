# -*- coding: utf-8 -*-
import functools

#写一个函数装饰器，来缓存函数的值

def cache(func):
    cache_dict = {}
#    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = repr(*args, **kwargs)
        if key in cache_dict:
            return cache_dict[key]
        else:
            #使用cache_dict缓存同一个sql的结果
            cache_dict[key] = func(*args, **kwargs)
            return cache_dict[key]
    wrapper.csrf_exempt = True
    functools.update_wrapper(wrapper, func)
    return wrapper

@cache
def execute_query(sql):
    print('hit db')
    return 'result'

#函数名是否发生变化，保持函数签名
print(execute_query)
# <function execute_query at 0xb709c89c>

print(execute_query('select * from table1'))
# hit db
# result

#缓存过的key不再缓存
print(execute_query('select * from table1'))
# result

print(execute_query('select * from table2'))
# hit db
# result

