# week01-summary

本周跟了week1的视频，因为之前有python的基础，所以再次学习就快多了。

相比较于之前的学习，也有一些不同的知识：

### 1.

```
Python中“if __name__=='__main__':”的作用
```

```
与Java、C、C++等几种语言不同的是，Python是一种解释型脚本语言，在执行之前不同要将所有代码先编译成中间代码，Python程序运行时是从模块顶行开始，逐行进行翻译执行，所以，最顶层（没有被缩进）的代码都会被执行，所以Python中并不需要一个统一的main()作为程序的入口。在某种意义上讲，“if __name__=='__main__':”也像是一个标志，象征着Java等语言中的程序主入口，告诉其他程序员，代码入口在此——这是“if __name__=='__main__':”这条代码的意义之一。
```

### 2.为什么头注释书写# coding=utf-8或者# coding:utf-8？

coding=utf-8的作用是：声明python代码的文本格式是utf-8编码，也即告诉python解释器要按照utf-8编码的方式来读取程序。

如果不加这个声明，无论代码中还是注释中有中文都会报错。

以下两种方式都可以声明：

(1)

```python
# coding=utf-8
 
a = 10
print '这是内容'
```

(2)

```python
# coding:utf-8
 
a = 10
print '这是内容'
```

#### 注意一点无论中间是‘：’还是‘=’，其中coding与它们之间都不能有空格。否则也会报错。

以上是针对Python2.x的版本而言，因为在Python2.x的版本中文本默认采用的是ASCII编码方式，而Python3.x的版本中，默认使用的就是UTF-8编码格式，所以就不需要在前面进行声明。
