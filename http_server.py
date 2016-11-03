# -*- coding: utf-8 -*-
# version: python 3.5
import threading
import re
import os
import sys

from wsgiref.simple_server import make_server
from file_util import *
from pydict_cn_bing_com import get_definition_cn_bing_com
from pydict_dict_youdao_com import get_definition_dict_youdao_com

"""
require lib(linux/mac):
pip3 install beautifulsoup4
pip3 install html5lib

require lib(windows):
python3 -m pip install beautifulsoup4
python3 -m pip install html5lib

browser URL:
http://localhost:8000/python_dictionary_online/test
"""

content_type_map = {
    'html': 'text/html; charset=utf-8',
    'js': 'application/x-javascript',
    'ico': 'image/x-icon',
    'css': 'text/css',
    'eot': 'font/opentype',
    'svg': 'text/xml',
    'ttf': 'application/x-font-ttf',
    'woff': 'application/x-font-woff',
    'woff2': 'application/font-woff2',
}

resource_path = 'D:\\GitHub\\PythonDictionary'
#resource_path = os.path.join(sys.path[0], 'resource')
print('resource_path:' + resource_path)


def get_url_map():
    result = {}
    files = []

    file_util_get_files(resource_path, files)
    for p in files:
        if file_util_get_ext(p) in content_type_map:
            p = p.replace('\\', '/')
            result[re.match('.*?(/resource/.*)', p).groups()[0]] = p
    return result


def application(environ, start_response):
    path_info = environ['PATH_INFO'].encode('iso8859-1').decode('utf-8')
    print(path_info)
    m = re.match('/(.*)/(.*)', path_info)
    dict = ''
    q = ''
    if m is not None:
        dict = m.groups()[0]
        q = m.groups()[1]

    url_map = get_url_map()

    if 'python_dictionary_online' == dict:
        start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
        html = file_util_read_text(os.path.join(resource_path, 'python_dictionary_online/index.html')).replace(
            '${python_dictionary_online_q}', q)
        return [html.encode('utf-8')]

    if 'cn_bing_com' == dict:
        start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
        return get_definition_cn_bing_com(q, os.path.join(resource_path, 'cn_bing_com'))

    if 'dict_youdao_com' == dict:
        start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
        return get_definition_dict_youdao_com(q, os.path.join(resource_path, 'dict_youdao_com'))

    if path_info in url_map:
        url_file = url_map[path_info]
        content_type = content_type_map.get(file_util_get_ext(url_file), 'text/html; charset=utf-8')
        start_response('200 OK', [('Content-Type', content_type)])
        return [file_util_read_byte(url_file)]

    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
    return [b'<h1>WSGIServer ok!</h1>']


# 新线程执行的代码
def loop():
    # 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
    httpd = make_server('', 8000, application)
    print("Serving HTTP on port 8000...")
    # 开始监听HTTP请求:
    httpd.serve_forever()


t = threading.Thread(target=loop, args=())
t.start()
