"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""

"""
如果为 True（默认值），该字段包含在生成的 repr() 方法返回的字符串中。
如果为 False，该字段不会包含在生成的 repr() 方法返回的字符串中。
"""
from dataclasses import dataclass, field


@dataclass
class Cat:
    name: str
    color: str
    # repr=False  在打印这个对象的时候，就不会包括这个字段
    weight: int =field(default=5)

cat = Cat("小橘", "yellow", 10)
print(cat)