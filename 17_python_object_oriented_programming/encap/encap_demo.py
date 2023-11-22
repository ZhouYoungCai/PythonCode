"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""


class Account:
    """账户"""

    # 普通属性
    bank = "BOC"

    # 保护属性（内部属性）
    _username = "Hogwarts"

    # 私有属性
    __password = "888"


    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        # 进行校验
        if len(value) >= 8:
            self.__password = value
        else:
            print("密码长度最少要有8位！")

# 实例化对象
obj = Account()

# 访问私有属性
# print(obj.password)

# 修改私有属性（满足校验条件）
# obj.password = "hogwarts666"
# print(obj.password)

# 修改私有属性（不满足条件）
obj.password = "123"
print(obj.password)