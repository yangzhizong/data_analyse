#!usr/bin/env python
#-*- coding:utf-8 _*-
"""

解析csv数据源为标准数据模板

"""
import pandas as pd
import time
import adapter_element
import pandas

# # 单py环境下测试使用参数
file_path=r'2018-04-08_15-23-03.csv'
input_data=pd.read_csv(file_path,engine='python',sep=';',encoding='utf-8',dtype=str)
input_params=''

def process(file_path,input_params,input_data):
    #取开始时间字符串
    begin_time = input_data['TimeStemp'][0].replace('_', '').replace(':','').replace('-','')
    #转为浮点型
    begin_time=float(begin_time)

    channels=[]
    first_cloumn = input_data.columns

    # 数据字段列表
    for i in first_cloumn:
        #调用common_30定制化数据模板，拿到channel对象
        channel=adapter_element.Channel()
        #设置没列对象属性
        channel.varname=i
        channel.varunit=''
        channel.t_start=begin_time
        channel.t_step = 20

        #设置每列数据对象的values值
        value_array=input_data[i].values
        #添加到channel.values列表
        for j in value_array:
            channel.values.append(j)

        channels.append(channel)


    return channels



if __name__ == '__main__':
    process(file_path, input_params, input_data)

