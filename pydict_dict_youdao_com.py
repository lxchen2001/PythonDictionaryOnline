# -*- coding: utf-8 -*-
# version: python 3.5
import urllib

from bs4 import BeautifulSoup
from file_util import *
from http_util import *
from beautiful_soup_util import *


def get_dict_html(word):
    """根据关键字得到有道翻译的例句并去除部分内容"""
    html = http_util_get_html('http://dict.youdao.com/w/%s' % urllib.parse.quote(word)).decode('utf-8')
    soup = BeautifulSoup(html, 'html5lib')
    content = None

    for e in soup.select('.trans-container'):
        content = e
        break

    bsu_del_attr_by_select_dict(content, {
        # '[style]': 'style',
    })

    bsu_del_ele_by_select_list(content, [
        # '.amend',
    ])
    return str(content)


def get_example_html(word):
    """根据关键字得到有道翻译的结果并去除部分内容"""
    html = http_util_get_html('http://dict.youdao.com/example/blng/eng/%s' % urllib.parse.quote(word)).decode('utf-8')
    soup = BeautifulSoup(html, 'html5lib')
    content = None

    for e in soup.select('#examples_sentences'):
        content = e
        break

    bsu_del_attr_by_select_dict(content, {
        '[onmouseout]': 'onmouseout',
        '[onmouseover]': 'onmouseover',
    })

    bsu_del_ele_by_select_list(content, [
        # '.amend',
    ])
    return '<div class="example-title">例句</div>' + str(content)


def get_definition_dict_youdao_com(word, resource_path):
    """根据关键字得到有道翻译的结果"""
    dict_html = get_dict_html(word)
    example_html = get_example_html(word)

    injection = []
    injection_html = ''

    file_util_get_files(resource_path, injection)

    for p in injection:
        if file_util_is_ext(p, 'html'):
            injection_html += file_util_read_text(p)

    return [bytes(dict_html + example_html + injection_html, encoding='utf-8')]
