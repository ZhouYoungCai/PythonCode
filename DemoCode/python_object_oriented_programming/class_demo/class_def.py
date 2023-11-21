"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""

# 类的声明
class Human(object):
    """人类"""

    # 定义属性（类属性）
    message = "这是类属性"


# 通过类名访问类属性
print(Human.message)