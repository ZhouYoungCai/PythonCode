"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
class Human:
    """人类"""

    # 类属性
    message = "这是Human类的属性"

    # 构造方法
    def __init__(self, name, age):
        # 实例属性
        self.name = name
        self.age = age

    # 实例方法
    def live(self):
        print("住在地球上")


class Student(Human):

    # 子类实例方法
    def study(self):
        print("正在学习")


# 实例化子类对象
stu = Student("哈利波特", 12)

# 访问属性
print(stu.message)
print(stu.name, stu.age)

# 访问实例方法
stu.live()
stu.study()
