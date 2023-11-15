t5 = 1, 2, 3
print(type(t5))  # 1、直接使用逗号分隔

t3 = (1, 2, 3)
print(t3)
t4 = ('a', 'b', 'c')
print(t4)  # 2、通过小括号填充元素

t1 = tuple()
print(type(t1))
t2 = tuple([1, 2, 3])
print(t2)
print(type(t2))  # 3、通过构造函数tuple()

tup6 = (1,)
print(type(tup6),tup6)  #注意，但元素元组，逗号不可缺少,不加逗号会认为是int类型


t = tuple('hogwarts')
print(t[2])  # 正向索引,打印g
print(t[-1])  # 反向索引，打印s

t = (1,2,3,4,5,6)
print(t[:])
print(t[:-2])
print(t[2:4])
print(t[2:5:2])

t = (1，3，2，3，2)
print(t.index(3))
t = ('h', 'o', 'g', 'w', 'a', 'r', 't', 's')   #元组常用方法index()    --index(item)
print(t.index('a'))   #返回与目标元素相匹配的首个元素的索引。目标必须在元组中存在的，否则会报错

"""元组使用：创建"""
# 1、直接使用逗号分隔
# tup1 = 1, 2, 3, 4, 5
# print(type(tup1), tup1)
# 2、通过小括号填充元素
# tup2 = (1, 2, 3, 4, 5)
# print(type(tup2), tup2)

# 3、通过构造函数tuple(iterable)
# tup3 = tuple()
# print(type(tup3), tup3)
# tup4 = tuple('hogwarts')
# print(type(tup4), tup4)
# tup5 = tuple([1, 2, 3, 4, 5])
# print(type(tup5), tup5)

# 4、注意：单元素元组，逗号不可或缺
# tup6 = 1,
# print(type(tup6), tup6)
# tup7 = (2,)
# print(type(tup7), tup7)
# tup8 = (3)
# print(type(tup8), tup8)

"""元组索引"""
# tup9 = tuple('hogwarts')
# # 1、正向索引
# print(tup9[2])
#
# # 2、反向索引
# print(tup9[-1])

"""元组切片"""
# 1、[start: stop: step]
# tup10 = tuple('hogwarts')
# print(tup10)
# print(tup10[0:3:1])
#
# print(tup10[::-1])
"""元组方法"""
# tup11 = tuple('hogowarts')
# 1、index(item)
# print(tup11.index('o'))
# print(tup11.index('x'))
# 2、count(item)
# print(tup11.count('o'))
# print(tup11)


"""元组解包"""
# tup12 = 1, 2, 3
# 1、传统逐个赋值的方式
# a = tup12[0]
# b = tup12[1]
# c = tup12[2]
# print(a, b, c)
# 2、解包平行赋值
# a, b, c = [1, 2, 3]
# print(a, b, c)
