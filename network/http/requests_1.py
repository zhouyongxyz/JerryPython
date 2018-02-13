#!/usr/bin/env python3
# coding:utf-8

import requests

# baidu_url = 'https://www.baidu.com'
#
# response = requests.get(baidu_url)
# print(response.content.decode())

base_url = 'https://www.baidu.com/s?wd=yitian'

params = {
    'wd': 'yitian'
}

response = requests.get(base_url)
print(response.url)
print(response.content.decode())