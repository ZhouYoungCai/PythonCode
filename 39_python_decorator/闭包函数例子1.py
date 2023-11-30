def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def makeitalic(fn):
    def wrapped() :
        return "<i>" + fn() + "</i>"
    return wrapped

@makebold()    #等同于 hello = makeitalic(hello)
@makeitalic()  #等同于 hello = makeitalic(hello)
def hello():
    return "hello world
print(hello()) #执行的并游 Line 21 的 hello()，而是 Line 19 的 hello()2526
#上述代码执行结果：<b><i>hello world</i></b>