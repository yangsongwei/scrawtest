'''
    func:装饰器练习
    author:monty
'''

import functools
import datetime
import numpy

#定义装饰器
def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print(func.__name__+" is run:"+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return func(*args,**kw)
    return wrapper

@log
def sum(a,b):
    print(a+b)


if __name__=='__main__':
    sum(1,2)

    sum(100,200)