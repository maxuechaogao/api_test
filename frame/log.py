#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import inspect
import sys
import logging.handlers
from colorama import Fore, Style


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
    return info[2]


def m2():
    m = get_func_called()
    m[2] = m[2].split('/')[-1]
    return m


plog_format = '%(asctime)s-%(levelname)s-%(message)s'
_logger = logging.getLogger('frame')
_logger.setLevel(logging.DEBUG)
_handler = logging.StreamHandler(sys.stdout)
_handler.setFormatter(logging.Formatter(plog_format))
_logger.addHandler(_handler)


def debug(msg):
    m = m2()
    _logger.debug(f'{m[2]}[{m[1]}]' + '-' + str(msg))


def info(msg):
    m = m2()
    _logger.info(Fore.GREEN + f'{m[2]}[{m[1]}]' + '-' + str(msg) + Style.RESET_ALL)


def error(msg):
    m = m2()
    _logger.error(Fore.RED + f'{m[2]}[{m[1]}]' + '-' + str(msg) + Style.RESET_ALL)


def warn(msg):
    m = m2()
    _logger.warning(Fore.YELLOW + f'{m[2]}[{m[1]}]' + '-' + str(msg) + Style.RESET_ALL)


def _print(msg):
    m = m2()
    _logger.debug(Fore.BLUE + f'{m[2]}[{m[1]}]' + '-' + str(msg) + Style.RESET_ALL)


def set_level(level):
    """ 设置log级别

    :param level: logging.DEBUG, logging.INFO, logging.WARN, logging.ERROR
    :return:
    """
    _logger.setLevel(level)


def set_level_to_debug():
    _logger.setLevel(logging.DEBUG)


def set_level_to_info():
    _logger.setLevel(logging.INFO)


def set_level_to_warn():
    _logger.setLevel(logging.WARN)


def set_level_to_error():
    _logger.setLevel(logging.ERROR)
