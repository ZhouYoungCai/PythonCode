"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
class Human:

    # 定义静态方法
    @staticmethod
    def grow_up():
        print("这是静态方法")

# 通过类名访问静态方法
Human.grow_up()

