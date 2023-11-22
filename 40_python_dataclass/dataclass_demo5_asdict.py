"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from dataclasses import dataclass, field, asdict


@dataclass
class Cat:
    name: str
    color: str = field(default="white")
    weight: int = field(default=2)
    # 可变参数 list, dict，需要通过 default_factory 来指定类型 或者默认值
    children: list = field(default_factory=list)

# asdict() 直接将实例对象转成字典格式
cat = Cat("小橘", "yellow", 10,[1,2,3])
print(asdict(cat))

