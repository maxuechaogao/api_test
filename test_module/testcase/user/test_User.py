#! /usr/bin/env python
# -*- coding: UTF-8 -*-

from test_module.pubilc import *
import json

class TestUser(publicFunc):

    def test_home(self):
        """
        用户-登录
        :return:
        """
        self.api_path = '/authService/getAuthPage'
        para = {
            'hid': 10126,
            'ids': '000001FF002940200001900372017845',
            'equType': 1
        }
        res = self.post_request(json.dumps(para))
        self.assertTrue(isinstance(res, dict))
        self.assertTrue(res.__contains__('errcode'), '返回值中不包含 code 字段')
        self.assertEqual(res['errcode'], 0, '请求异常')
