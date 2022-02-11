import xlrd   #引入库

wb=xlrd.open_workbook("F:/研究生0年级/task/FX034290.xls") #打开文件并返回一个工作蒲对象。open_workbook可以点进去看看函数里面的参数的含义之类的，很详细，英语不好的可以百度翻译，翻译出来的结果差不多。
sheet_num=wb.nsheets  #获取excel里面的sheet的数量
sheet_names=wb.sheet_names()   #获取到Excel里面所有的sheet的名称列表，即使没有sheet也能用。
sheet=wb.sheet_by_index(0)   #通过索引的方式获取到某一个sheet，现在是获取的第一个sheet页，也可以通过sheet的名称进行获取，sheet_by_name('sheet名称')
rows=sheet.nrows   #获取sheet页的行数，一共有几行
print(rows)
columns=sheet.ncols   #获取sheet页的列数，一共有几列
#获取第一行的数据
row_data=sheet.row_values(0)  #返回给定的行数的单元格数据进行切片
print(row_data)
#获取第二列的数据
col_data=sheet.col_values(1)
#获取单元格的数据
one_data=sheet.cell(0,1)  #同样是通过索引的方式，cell(0,1)获取到的是第一行第二列的单元格数据
cell_value=one_data.value  #获取单元格的值
print(cell_value)
# cell_type=one_data.ctype   #获取单元格的类型，在xlrd中，单元格的数据类型有6种，
# 0  --  空（empty）
# 1  --  字符串（string）
# 2  --  数字（number）
# 3  --  date（日期）
# 4  --  boolean（布尔值）
# 5  --  error（错误）
