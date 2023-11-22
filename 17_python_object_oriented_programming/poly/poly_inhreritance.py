"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
class Human:

    message = "这是Human类的属性"

    # 构造方法
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 实例方法
    def live(self):
        print("住在地球上")


class Student(Human):
    """学生类"""

    # 重写父类构造方法
    def __init__(self, name, age, school):
        # 访问父类的构造方法
        # super().__init__(name, age)
        # super(Student, self).__init__(name, age)
        Human.__init__(self, name, age)
        self.school = school

    # 重写父类实例方法
    def live(self):
        print(f"住在{self.school}")


# 实例化子类对象
stu = Student("哈利波特", 12, "hogwarts")
print(stu.name)

# 访问重写的实例方法
stu.live()