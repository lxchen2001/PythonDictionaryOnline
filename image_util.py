# -*- coding: utf-8 -*-
# version: python 3.5
import base64
from urllib import request


def image_util_get_image_mime(base64_data):
    """根据base64字符串得到图片的content_type"""
    if base64_data[0] == '/':
        return 'image/jpeg'
    elif base64_data[0] == 'R':
        return 'image/gif'
    elif base64_data[0] == 'i':
        return 'image/png'


def image_util_get_image_base64(url):
    """下载指定url图片并返回含“data:xxx”的图片base64字符串"""
    req = request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (iPad; CPU OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1')

    with request.urlopen(req) as f:
        rst_bytes = bytes()
        for line in f:
            rst_bytes += line
        base64_image = base64.b64encode(rst_bytes).decode('utf-8')
    return 'data:%s;base64,%s' % (image_util_get_image_mime(base64_image), base64_image)
