"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from dataclasses import dataclass, field


# @dataclass
# class Cat:
#     name: str
#     color: str = field(default="white")
#     weight: int = field(default=2)
#     # 可变参数 list, dict，需要通过 default_factory 来指定类型 或者默认值
#     children: list = field(default_factory=list)


@dataclass
class Cat:
    name: str
    color: str
    # init=False  在实例化对象的时候， 不需要设置这个值，需要给一个默认值
    weight: int =field(default=5,init=False)
    # 可变参数 list, dict，需要通过 default_factory 来指定类型 或者默认值
    # children: list = field(default_factory=list)
"""
如果为 True（默认值），该字段作为参数包含在生成的 init() 方法中。
如果为 False，该字段不会包含 init() 方法参数中。

体现在：在实例化的时候，是否需要传递这个参数
"""
cat = Cat(name="喵喵",color="black")
print(cat)

