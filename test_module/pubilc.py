#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import inspect
import unittest
from frame import *
import requests
from urllib import parse, request


class publicFunc(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        self.domain = 'https://japauth.superhcloud.com'
        # 公共API路径
        self.public_api_path = ''
        # 特定API路径以用例中为准
        self.api_path = ''
        self.token = ''

    def get_request(self, params=None, **kwargs):
        url = self.domain + self.public_api_path + self.api_path
        log.debug('get_request  url:{},param:{}'.format(url, params))
        try:
            response = requests.get(url, params=params, timeout=(2, 4), **kwargs)
            if response.status_code != 200:
                with open('./err.html', 'wb') as f:
                    for i in response.iter_content(chunk_size=512):
                        f.write(i)
                raise ValueError
            else:
                res = response.json()
                log.debug(f'get_response {res}')
            return res
        except Exception as e:
            log.error("get_request_error {}".format(e))
            raise e

    def get_request_urllib(self, params=None):
        textmod = parse.urlencode(params)
        url = self.domain + self.public_api_path + self.api_path
        header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}
        req = request.Request(url="{}?{}".format(url, textmod), headers=header_dict)
        res = request.urlopen(req)
        res = res.read()
        # return res
        return res.decode(encoding='utf-8')

    def post_request(self, params=None, json=None, **kwargs):
        url = self.domain + self.public_api_path + self.api_path
        if kwargs:
            log.debug('post_request  url:{},kwargs:{}'.format(url, kwargs))
        else:
            log.debug('post_request  url:{},param:{}'.format(url, params))
        try:
            response = requests.post(url, data=params, json=json, timeout=(2, 4), **kwargs)
            res = response.json()
            log.debug(f'post_response {res}')
            return res
        except Exception as e:
            log.error("post_request_error:{}".format(e))
            raise e

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass
