# coding:utf-8


class Person(object):
    name = None
    age = None

    def run(self):
        print("{}在奔跑".format(self.name))
    def jump(self):
        print("{}在跳跃".format(self.name))
    def work(self):
        self.run()
        self.jump()


    def test(self):
        self.run()
        print(self.name)




# 实例化类
# 对象zxy
zxy = Person()
zxy.name = "zxy"
zxy.run()
zxy.jump()

lss = Person()
# 只是实例化了，但是没有赋值属性，所以打印的还是None
lss.run()
# 属性赋值
lss.name = "lss"
lss.run()
lss.jump()

# 实例化吕雪阳
lxy = Person()
# 可以给实例化对象添加属性，不会影响类和其他实例化对象
lxy.height = 175
print(lxy.height)
# print(zxy.height)  # 报错：AttributeError: 'Person' object has no attribute 'height'

print("-" * 100)
zxy.work()


# 注意点:
# 在类中，self是属性、方法之间的调用的桥梁
# 在类函数中要想调用其他类函数和类属性，就必须使用self