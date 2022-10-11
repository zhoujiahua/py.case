#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import time
from functools import wraps


def decorator(func):
    @wraps(func)
    def wrapper(*args, **kw):
        print(time.time())
        func(*args, **kw)

    return wrapper


@decorator
def f1(a):
    print(f'{f1.__name__}:{a}')


f1('123')
