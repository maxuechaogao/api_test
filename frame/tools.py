#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import inspect
from contextlib import contextmanager

__author__ = 'xcma'
import functools
from . import log


def get_func_called():
    """
    获取当前方法被调用路径,从1开始，因为0是自己，不能被用作公共方法
    :return:
    """
    src = inspect.stack()
    info = []
    for i in range(1, len(src)):
        func_name = src[i][3]
        func_path = src[i][1]
        func_line = src[i][2]
        if not func_name.count('<') and not func_path.count('python2.7'):
            called_func_info = [func_name, func_line, func_path]
            info.append(called_func_info)
    return info[1]


def printFuncName(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        fname = get_func_called()
        log.info(f'-----start:{fname[0]}----')
        fres = func(*args, **kwargs)
        log.info(f'-----end:{fname[0]}------')
        return fres
    return wrapper
