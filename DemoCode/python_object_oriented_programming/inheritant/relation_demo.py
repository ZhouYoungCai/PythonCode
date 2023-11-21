"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""

# 人类
class Human:
    pass

# 学生类
class Student(Human):
    pass

# 老师类
class Teacher(Human):
    pass


# 检查实例VS类
stu = Student()
# print(isinstance(stu, Human))

# 检查类VS类
print("Student:Human", issubclass(Student, Human))
print("Student:Teacher", issubclass(Student, Teacher))