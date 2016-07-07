# -*- coding: utf-8 -*-
# version: python 3.5
from urllib import request


def http_util_get_html(url):
    """得到指定url返回byte"""
    req = request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (iPad; CPU OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1')

    with request.urlopen(req) as f:
        rst_bytes = bytes()
        for line in f:
            rst_bytes += line
    return rst_bytes
