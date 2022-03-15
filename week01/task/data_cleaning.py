# 去0  保证发动机油温 发动机运行时间 机油压力 冷却剂温度 瞬时油耗 扭矩 整车负荷率 转速  车速  无0
import numpy as np
import pandas as pd
import openpyxl
from pandas import Series, DataFrame
# iris_data = pd.read_excel("../data/day03/FX034290.xls")
# iris_data = pd.read_excel(io=r'F:\研究生0年级\task\王师姐相关任务\FX034290.xls')
iris_data = pd.read_excel('F:/研究生0年级/task/王师姐相关任务/FX034290.xls')
data=iris_data.drop(["大气压力","进气温度","尿素液位","燃油累计使用量","蓄电池电压","发动机运行时间",],axis=1)
print(type(data))
# 清除车速大于120的行
data =data.drop(data[data['车速'] > 120].index)
# data=iris_data.drop(["大气压力","发动机运行时间","进气温度","尿素液位","燃油累计使用量","蓄电池电压","发动机运行时间","精度","维度","高度","里程(公里)"," 定位标记","南北纬标记","东西经标记",],axis=1)
data3=data[-data.发动机油温.isin([0])]
# data4=data3[-data3.发动机运行时间.isin([0])]
data4=data3[-data3.机油压力.isin([0])]
data5=data4[-data4.冷却剂温度.isin([0])]
data6=data5[-data5.瞬时油耗.isin([0])]
data7=data6[-data6.扭矩.isin([0])]
#data9=data8[-data8.蓄电池电压.isin([0])]
data8=data7[-data7.整车负荷率.isin([0])]
data9=data8[-data8.转速.isin([0])]
# data10=data9[-data9.车速.isin([0])]
print(data9)
print(type(data9))

# writer = pd.ExcelWriter('F:\task\result.xlsx')
# data.to_excel(writer, sheet_name='nozero')
# writer.save()

data9.to_excel('F:/task/result.xlsx')

# create and writer pd.DataFrame to excel
# writer = pd.ExcelWriter('../data cleaning/consequence/' + file_name.split('.')[0] + '-1.xls')
# writer.save()