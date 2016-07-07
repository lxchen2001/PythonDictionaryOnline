# -*- coding: utf-8 -*-
# version: python 3.5


def bsu_del_ele_by_select(dom, select):
    """根据css选择器删除元素"""
    for e in dom.select(select):
        e.extract()


def bsu_del_ele_by_select_list(dom, select_list):
    """根据css选择器list删除元素"""
    for s in select_list:
        bsu_del_ele_by_select(dom, s)


def bsu_del_attr_by_select(dom, select, attr):
    """根据css选择器删除指定属性"""
    for e in dom.select(select):
        del e[attr]


def bsu_del_attr_by_select_dict(dom, select_dict):
    """根据css选择器dict删除指定属性"""
    for select, attr in select_dict.items():
        bsu_del_attr_by_select(dom, select, attr)
