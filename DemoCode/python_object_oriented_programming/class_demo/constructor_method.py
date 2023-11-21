"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""

class Human:

    # 定义属性
    message = "这是类属性"

    # 定义构造方法
    def __init__(self, name, age):
        # 实例属性(变量)
        self.name = name
        self.age = age
        print("这是构造方法")


# 实例化对象
person = Human("哈利波特", 12)

# 通过实例访问类属性
print(person.message)
# 通过实例访问实例属性
print(person.name)
print(person.age)