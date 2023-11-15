#coding:utf-8
from pytest import *

li1 = list()  # 空列表，创建列表
li2 = list('hogwarts')  # 字符串，创建列表
li3 = list((1, 2, 3))  # 元组，创建列表
li4 = list({4, 5, 6})  # 集合，创建列表
li5 = list({'a': 7, 'b': 8})  # 字典，创建列表
print(type(li1), li1,type(li2), li2,type(li3), li3,type(li4), li4,type(li5), li5)


li6 = [1,2,3,4,5]
print(li6[0])  # 打印1,索引的使用
print(li6[3])  # 打印4,索引的使用
print(f"list6最后一个元素是：",li6[-1])  # 打印5,索引的使用


list7 = [1,2,3]
print(f"判断1在list7里面：",1 in list7)      # 成员检测，in：检查一个元素是否在列表中
print(f"判断2不在list7里面：",2 not in list7)  # 成员检测，，not in：检查一个元素不在列表中

list11 = [3]
print(list11 * 7)  # *乘号的使用

list12 = [1,2,3]
list13 = [4,5,6]
print(f"list12+list13的值是：",list12 + list13)  # +加号的使用

list8 = [1,2,3]
list8.append("hogwarts")  # append():append方法讲一个对象添加到列表的末尾
print(f"list8.append后的结果是：",list8,f"list8.append后的长度是：",len(list8))

list9 = [1,2,3]
list10 = [4,5,6]
list9.extend(list10)  # extend():extend方法将一个可迭代对象的所有元素，添加到列表末尾
list10.extend("789")  # extend():extend方法将一个可迭代对象的所有元素，添加到列表末尾
print(f"list9.extend后的结果是：",list9)
print(f"list10.extend后的结果是：",list10)

list14 = [0,1,2]
print("插入前:",list14)  # 打印 [0，1，2]
list14.insert(0,"hogwarts")
print("插入后:",list14) # 在索引0的位置插入元素,打印 ['hogwarts’，0，1，2]

letters = ['h', 'o', 'g', 'w', 'a', 'r', 't', 's']
n1 = letters.pop(3)
print(f"n1的值是：",n1)  # 打印w,# 传入索引3，弹出元素,列表方法pop()的使用：弹出并返回所指定索引的元素
n2 = letters.pop()
print(f"n2的值是：",n2)  # 打印s,不传参数，默认弹出末尾元素,列表方法pop()的使用：弹出并返回所指定索引的元素
print(f"letters的最新值是：",letters)   # 弹出所指定索引的元素，w和s，打印['h', 'o', 'g', 'a', 'r', 't']