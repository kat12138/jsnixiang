#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/23 00:52 AM
# @Author  : Zhangjing
# @File    : test.py

import time
from hashlib import md5
import requests
import random
# print(time.time(),len(str(time.time())))
#
# str1 = "123"
# md = md5()
# md.update(str1.encode())
# res = md.hexdigest()
# print(res,len(res))

# python复写数据处理部分
headers = {
  'Connection': 'keep-alive',
  'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
  'Accept': 'application/json, text/javascript, */*; q=0.01',
  'X-Requested-With': 'XMLHttpRequest',
  'sec-ch-ua-mobile': '?0',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'Origin': 'https://fanyi.youdao.com',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Dest': 'empty',
  'Referer': 'https://fanyi.youdao.com/',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'Cookie': 'OUTFOX_SEARCH_USER_ID=1540878140@10.108.160.101; JSESSIONID=aaak1TOepBggEeMvxA0Ox; OUTFOX_SEARCH_USER_ID_NCOO=1565187648.2040107; ___rl__test__cookies=1624378249049'
}

word = input("please input your tanslate word")
ts = str(int(time.time()*1000))
salt = ts+str(random.randint(0,9))
str1 = "fanyideskweb" + word + salt + "Tbh5E8=q6U3EXe+&L[4c@"
md = md5()
md.update(str1.encode())
sign = md.hexdigest()
data = "i="+word+"&from=AUTO&to=AUTO&smartresult=dict&client=fanyideskweb&salt="+salt+"&sign="+sign+"&lts="+ts+"&bv=35b48b2871e19cf5e4fb073019371d86&doctype=json&version=2.1&keyfrom=fanyi.web&action=FY_BY_CLICKBUTTION"
html = requests.post(url = "https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule",headers=headers,data=data).json()
print(html)
