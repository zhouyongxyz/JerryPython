# -*- coding: UTF-8 -*-
# 引入文字识别OCR SDK
from aip import AipOcr

# 定义常量
APP_ID = '10079802'
API_KEY = 'wWVNwwHG4tOsOmX7cXMOIgQR'
SECRET_KEY = 'z7F4gNiPkAwQfxtnccdOd842I8SUrVDl'

# 读取图片
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def main():
    # 初始化ApiOcr对象
    aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    # 定义参数变量
    options = {
        'detect_direction': 'true',
        'language_type': 'CHN_ENG',
    }
    # 调用通用文字识别接口
    result = aipOcr.basicGeneral(get_file_content('../songti.jpeg'),options)

    # 如果图片是url 调用示例如下
    #result = aipOcr.basicGeneral('http://www.xxxxxx.com/img.jpg')
    print result
    print result['words_result'][0]['words']

if __name__ == "__main__":
    main()