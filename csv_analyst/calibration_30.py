#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
筛选计算数据

"""
import pandas as pd
import os
import adapter_element


# 清洗values数据
def float_value(v):
    try:
        return float(v)
    except ValueError:
        return float(0)


def process(file_path,input_params,input_data):
    #数据源中不需要标定输出的字段
    csv_delete=['W_AcPower','W_Nac_AccZ','Bl2_I_40M','Bl1_25M','Bl2_B6_40M','Bl2_S1_20M1','Bl3_S1_12M1.1'] #注意还有

    #删除2个时间列
    input_data.pop(0)
    input_data.pop(0)

    for i in input_data:
        # print(i.varname)
        #删除无用的字段
        # print(i.values)
        if i.varname in csv_delete:
            input_data.remove(i)

        i.values = [float_value(each) for each in i.values]

        #添加变量单位、计算
        #m/s
        if i.varname == 'M_Main_WS' or i.varname == 'M_Ref_WS' or  i.varname == 'M_Tip_WS' or i.varname == 'W_Nac_WS':
            i.varunit='m/s'
            if i.varname == 'W_Nac_WS':
                for j in range(len(i.values)):
                    i.values[j]=i.values[j] / 100

        #m/s^2
        elif i.varname == 'W_Nac_AccX' or i.varname == 'W_Nac_AccY':
            i.varunit='m/s^2'
            for j in range(len(i.values)):
                i.values[j] = i.values[j] / 1000

        #deg
        elif i.varname == 'M_Main_WD':
            i.varunit = 'deg'


        elif i.varname == 'W_Rotor_Pos' or i.varname == 'W_Pitch1' or i.varname == 'W_Pitch2' or i.varname == 'W_Pitch3' or i.varname == 'W_Pitch1_Set' or  i.varname == 'W_Pitch2_Set' or i.varname == 'W_Pitch3_Set' or i.varname == 'W_NAC_WD' or i.varname == 'W_NAC_VD':
            i.varunit = 'deg'
            for j in range(len(i.values)):
                i.values[j] = i.values[j] / 100


        elif i.varname ==  'W_Yaw_Pos':
            i.varunit = 'deg'
            for j in range(len(i.values)):
                i.values[j] = i.values[j] / 10

        #rpm
        elif i.varname == 'W_Rotor_SP' or i.varname == 'W_Gen_SP':
            i.varunit = 'rpm'
            if i.varname == 'W_Rotor_SP':
                for j in range(len(i.values)):
                    i.values[j] = i.values[j] / 100
            else:
                for j in range(len(i.values)):
                    i.values[j] = i.values[j] / 10

        #Nm
        elif i.varname == 'W_Gen_Tor':
            i.varunit = 'Nm'
            for j in range(len(i.values)):
                i.values[j] = i.values[j]

        elif i.varname == 'W_Gen_Tor_Set':
            i.varunit = 'Nm'

        #-
        elif i.varname == 'W_GD' or i.varname == 'W_Yaw_CCW' or i.varname == 'W_Yaw_CW':
            i.varunit = '-'

        # ℃
        elif i.varname == 'M_Temp':
            i.varunit = '℃'

        # %
        elif i.varname == 'M_Humi':
            i.varunit = '%'

        #hPa
        elif i.varname == 'M_Press':
            i.varunit = 'hPa'

        #kW
        elif i.varname == 'Power' or i.varname == 'W_Gen_APower':
            i.varunit = 'kW'


    for k in input_data:
        if k.varname == 'Bl2_O_40M':
            input_data.remove(k)

    # 再次对空数据和str类型清洗

    for v in input_data:
        if type(v.values[0]) == str or type(v.values[0] == int):
            for values_index in range(len(v.values)):
                if v.values[values_index] == 'None':
                    v.values[values_index] = '0'
            v.values=list(map(float,v.values))


    return input_data
