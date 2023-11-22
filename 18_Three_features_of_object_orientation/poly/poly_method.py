"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
class China:
    def speak(self):
        print("汉语")

class Usa:
    def speak(self):
        print("English")


# 实例化对象
cn = China()
us = Usa()

# 遍历
for x in (cn, us):
    x.speak()