#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:xiaowei.han
@file: adapter_element.py
@time: 2018/12/19 10:49

"""
class Channel(object):
    '''

    '''

    def __init__(self):
        '''

        '''
        #变量名称
        self.varname = ''
        #变量单位
        self.varunit = ''
        #变量时序值
        self.values = []
        #起始时间
        self.t_start = 0.0
        #间隔时间
        self.t_step = 0.0
