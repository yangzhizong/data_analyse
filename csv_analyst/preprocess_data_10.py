#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
获取文件提取文件开始时间

"""
import time
import pandas as pd
import pandas

#单py环境下测试使用参数
# file_path=r'D:\G04\csv\2018-04-08_15-23-03.csv\2018-04-08_15-23-03.csv'
# input_data=pd.read_csv(file_path,engine='python',sep=';',encoding='utf-8',dtype=str)
# input_params=''


def process(file_path,input_params,input_data):
    timestr="0"
    #读到原始时间数据
    begin_time=input_data['TimeStemp'][0]
    #输出字符串格式的年月日时分秒
    timestr=begin_time.replace('-','').replace('_','').replace(':','')
    timestr=timestr.split('.')[0]

    return timestr



# if __name__ == '__main__':
#     process(file_path, input_params, input_data)
#
