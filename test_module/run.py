#! /usr/bin/env python
# -*- coding: UTF-8 -*-

from frame import *

if __name__ == '__main__':
    setting.run_case = {Tag.ALL}  # 运行全部测试用例
    runner = TestRunner()
    runner.add_case_dir(r"testcase")
    runner.run_test(report_title='接口自动化测试报告')
