# -*- coding: utf-8 -*-
# version: python 3.5
import urllib

from bs4 import BeautifulSoup
from file_util import *
from http_util import *
from beautiful_soup_util import *


def get_definition_cn_bing_com(word, resource_path):
    """根据关键字得到必应翻译的结果并去除部分内容"""
    html = http_util_get_html('http://cn.bing.com/dict/search?q=%s' % urllib.parse.quote(word)).decode('utf-8')
    soup = BeautifulSoup(html, 'html5lib')
    content = None

    for e in soup.select('.lf_area'):
        content = e
        break

    bsu_del_attr_by_select_dict(content, {
        '[style]': 'style',
        'a[href*="/dict"]': 'href',
        'a[href*="/search"]': 'href',
        'a[onmousemove*="alignWords"]': 'onmousemove',
        'a[onclick*="BilingualAjax"]': 'onclick',
        'a[title="点击朗读"]': 'title',
    })

    bsu_del_ele_by_select_list(content, [
        '#defid',
        '.wd_div',
        '.df_div',
        '.filter',
        '#filshow',
        '#filhide',
        '.bi_pag',
        '#loaddataid',
        '.hd_area',
    ])

    injection = []
    injection_html = ''

    file_util_get_files(resource_path, injection)

    for p in injection:
        if file_util_is_ext(p, 'html'):
            injection_html += file_util_read_text(p)

    return [bytes(str(content) + injection_html, encoding='utf-8')]
