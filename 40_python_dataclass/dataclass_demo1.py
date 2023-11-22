"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from dataclasses import dataclass
# 1.加类装饰器 @dataclass
# 2. 为类变量添加类型提示
@dataclass
class Cat:
    name: str
    color: str
    weight: int

if __name__ == '__main__':
    cat = Cat("菠萝", "橘猫", 9)
    print(cat)