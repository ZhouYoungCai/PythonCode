def timer(func):
    def inner():
        print("计时开始")
        func()
        print("计时结束")
    return inner

@timer
def hogwarts():
    print("霍格沃兹测试学院")

hogwarts()