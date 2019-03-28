import pandas as pd
import preprocess_data_10
import transfer_raw_data_to_struct_data_20
import calibration_30


#数据源测试
file_path='2018-04-08_15-13-03.csv'
input_data=pd.read_csv(file_path,engine='python',sep=';',encoding='utf-8')
input_params=''


#第一步：输出表格开始时间（字符串格式）
timestr=preprocess_data_10.process(file_path,input_params,input_data) ##输出结果要年月日时分秒字符串 例如：20180408154431
# print('第一步：输出开始时间：',timestr)


#第二步：解析数据源为标准数据模板
channels=transfer_raw_data_to_struct_data_20.process(file_path,input_params,input_data)
# print('第二步：源channels数据对象列表',channels)


#第三步：计算数据输出标定后的模板数据
output_data=calibration_30.process(file_path,input_params,channels)
print('第三步：计算后的channels数据对象列表：',output_data)










