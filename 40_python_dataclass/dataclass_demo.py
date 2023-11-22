"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
class Cat:
    name: str
    color: str
    weight: int

    def __init__(self,name,weight,color):
        self.name = name
        self.weight = weight
        self.color = color

    def __str__(self):
        return f"喵星人姓名：{self.name}, 年龄：{self.weight}，颜色：{self.color}"

    def __repr__(self):
        return f"===>>>>> 喵星人姓名：{self.name}, 年龄：{self.weight}，颜色：{self.color}"
if __name__ == '__main__':
    cat =Cat("大橘",10, "橘色")
    print(cat)