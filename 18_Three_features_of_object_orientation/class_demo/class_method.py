"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""

class Human:

    # 类属性
    population = 0

    # 类方法
    @classmethod
    def born(cls):
        print("这是类方法")
        cls.population += 1

# 通过类名访问类方法
Human.born()
print(Human.population)