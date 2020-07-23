#! /usr/bin/env python
# -*- coding: UTF-8 -*-
"""
单独使用测试报告组件，不需要utx的其他扩展功能
"""
import frame

if __name__ == '__main__':

    frame.stop_patch()

    runner = frame.TestRunner()
    runner.add_case_dir(r"testcase\chat")
    runner.run_test(report_title='接口自动化测试报告')