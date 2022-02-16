import pandas

data = pandas.DataFrame({
    'id': [1, 2, 3],
    'name': ['user', 'admin', 'nothing'],
    'age': [18, 20, 11],
    'city': ['北京', '上海', '深圳']
})
data = data.set_index('id')
print(data)

data.to_excel('F:/task/result.xlsx')
print('write done!')