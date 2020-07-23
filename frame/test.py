#! /usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = 'xcma'
class Counter:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)


def todo(func):
    import functools
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        return func(*args,**kwargs)
    return wrapper


@todo
def foo(a,b):
    return a+b
#
# for i in range(10):
#     res = foo(i,i+1)
#     if res==5:
#         print(f'*****')
#     else:
#         print(res)



a = '/Users/maxuechao/code/api_test/frame/runner.py'
print(a.split('/')[-1])