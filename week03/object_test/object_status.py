# coding:utf-8

"""
    多态
    就是子类中与父类中同一个方法（同一个方法名）
    但是执行出来的内容不同

    为什么使用继承？
    写好了一个类，之后的类需要的功能和之前的类非常相似，我们就不需要重复写一样的代码了
    直接通过继承，就可以使用父类中的方法和属性，可以提高代码的重用！！！
    为什么使用多态？
    子类继承了父类中的方法，一部分我直接用就OK，但是有一部分我想要有些改变（“取其精华，去其糟粕”）
    所以虽然有些子类和父类的方法名一样，但是我可以通过重写（多态）来使得子类不同于（或者说优于）继承自父类的方法
"""

# 父类
class Parent(object):
    def talk(self):
        print("父母在说....")


# 子类1
class Brother(Parent):
    def run(self):
        print("哥哥在奔跑....")
    # 重写继承自父类的talk方法
    def talk(self):
        print("哥哥在说....")


# 子类2
class Me(Parent):
    # 重写继承自父类的方法
    def talk(self):
        print("我说自己的观点....")






if __name__ == "__main__":
    b = Brother()
    b.run()
    b.talk()

    # 实例化父类
    p = Parent()
    p.talk()

    # 实例化子类2
    m = Me()
    m.talk()
