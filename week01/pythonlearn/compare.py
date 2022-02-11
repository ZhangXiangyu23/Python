# coding:utf-8

a = 1
a_01 = 1
b = 2

print(a == a_01)
print(a == b)
# 判断地址是否相同，应该使用is
print(a is a_01)
print('a的地址是', id(a))
print('a_01的地址是', id(a_01))

# 如果在python解释器里面运行的话
# 会返回False,因为在python解释器中，只对0~255的值提前固定了地址，超过255的数没有固定地址
# 在pycharm中，返回True的原因是，上一行的f已经将300放在一个地址
# 下面的f_01直接使用了上面f地址中的300，所以两个地址一样！！！
f = 300
f_01 = 300
print(f is f_01)

print(id(f))
print(id(b))
print(f is not b)
