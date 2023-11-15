#coding:utf-8
from pytest import *

li1 = list()  # 空列表，创建列表
li2 = list('hogwarts')  # 字符串，创建列表
li3 = list((1, 2, 3))  # 元组，创建列表
li4 = list({4, 5, 6})  # 集合，创建列表
li5 = list({'a': 7, 'b': 8})  # 字典，创建列表
print(type(li1), li1)
print(type(li2), li2)
print(type(li3), li3)
print(type(li4), li4)
print(type(li5), li5)

li6 = [1,2,3,4,5]
print(li6[0])  # 打印1,索引的使用
print(li6[3])  # 打印4,索引的使用
print(li6[-1])  # 打印5,索引的使用


list7 = [1,2,3]
print(1 in list7)      # 成员检测，in：检查一个元素是否在列表中
print(2 not in list7)  # 成员检测，，not in：检查一个元素不在列表中

list8 = [1,2,3]
list8.append("hogwarts")  # append():讲一个对象添加到列表的末尾
print(list8)

list9 = [1,2,3]
list10 = [4,5,6]
list9.extend("list10")  # extend():将一个可迭代对象的所有元素，添加到列表末尾
print(list9)

list11 = [3]
print(list11 * 7)  # *乘号的使用

list12 = [3,4,5]
list13 = [1,2,6]
print(list12 + list13)  # +加号的使用