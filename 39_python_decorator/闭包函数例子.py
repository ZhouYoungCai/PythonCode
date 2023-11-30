'''
闭包函数定义
在通过Python的语言介绍一下，一个闭包就是你调用了一个函数A，这个函数A返回了一个函数B给你。
这个返回的函数B就叫做闭包。你在调用函数A的时候传递的参数就是自由变量。
这里面调用func的时候就产生了一个闭包——inner_func,并且该闭包持有自由变量——name，
因此这也意味着，当函数func的生命周期结束之后，name这个变量依然存在，因为它被闭包引用了，所以不会被回收。
'''
def func(name):
    def inner_func(age):
        print('name:', name, 'age:', age)
    return inner_func

bb = func('the5fire')
bb(26)  # >>> name: the5fire age: 26