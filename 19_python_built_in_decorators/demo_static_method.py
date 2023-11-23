#coding:utf-8
"""
静态方法：多轮比赛，每轮由两个不同的英雄对打
"""
class Game:

    def __init__(self, first_hero, second_hero):
        self.first_hero = first_hero
        self.second_hero = second_hero
    # fight 有和实例变量交互的部分，所以需要定义为一个普通方法
    def fight(self):
        print(f"本轮比赛开始，由{self.first_hero} VS {self.second_hero}")

    # start 没有和类或实例交互的部分，那么就可以使用staticmethod
    @staticmethod
    def start():
        print("游戏开始")

Game.start()
game1 = Game("Bob", "Mary")
game2 = Game("Mike", "Henry")
game1.fight()
game2.fight()

'''
实际案例
下面的代码实现的需求是格式化输出时间
如果现在需求变更，输入 年、月、日 没法保证格式统一，
可能是json，可能是其他格式的字符串，在不修改构造函数的前提下，如何更改代码
'''
class DateFormat:
    def __init__(self, year=0, month=0, day=0):
        self.year = year
        self.month = month
        self.day = day

    def out_date(self):
        return f"输入的时间为{self.year}年，{self.month}月，{self.day}日"


year, month, day = 2017, 7, 1

demo = DateFormat(year, month, day)
print(demo.out_date())