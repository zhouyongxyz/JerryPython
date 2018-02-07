# /usr/bin/env python
# coding=utf8

import httplib
import md5
import urllib
import random
import json

appid = '20170901000079608'
secretKey = 's3TzQi4Zs7tRc7KMsGiZ'

httpClient = None
myurl = '/api/trans/vip/translate'
q = '你最近在干嘛？'
fromLang = 'zh'
toLang = 'en'
salt = random.randint(32768, 65536)

def main():
    sign = appid + q + str(salt) + secretKey
    m1 = md5.new()
    m1.update(sign)
    sign = m1.hexdigest()
    myurl1 = myurl + '?appid=' + appid + '&q=' + urllib.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
        salt) + '&sign=' + sign

    try:
        httpClient = httplib.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl1)

        # response是HTTPResponse对象
        response = httpClient.getresponse()
        result = json.loads(response.read());
        #print response.read()
        #print result
        print result['trans_result'][0]['dst']

    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()

if __name__ == "__main__":
    main()