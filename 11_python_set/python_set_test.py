"""集合创建"""
# 1、通过使用`{}`填充元素
set1 = {1, 2, 3}
print(f"这是set1",set1, type(set1))

# 2、通过构造方法 set(iterable)
set2 = set('hogwarts')
print(f"这是set2",set2, type(set2))
set3 = set([1, 2, 3])
print(f"这是set3",set3, type(set3))
set4 = set()
print(f"这是set4",set4, type(set4))

# 3、通过集合推导式
set5 = {i for i in range(5) if i % 2 == 0}
print(f"这是set5",set5, type(set5))


"""集合使用"""
set6 = {1, 4, 6}
# # 1、in
print(f"这是set6，1 in set6",1 in set6)
# # 2、not in
print(f"这是set6，100 not in set6",100 not in set6)


"""
集合方法，一共6个；
add()：将单个对象添加到集合中
update()：批量添加来自可迭代对象中的所有元素
remove()：从集合中移除指定元素
discard()：从集合中移除指定对象
pop()：随机从集合中移除并返回一个元素
clear()：清空集合，移除所有元素
"""
set7 = set()
'''1、add方法：add(item)'''
set7.add(1)
set7.add(2)
set7.add('hogwarts')
print(f"add方法，这是set7", set7,type(set7))
'''2、update方法：update(iterable)'''
set7.update('hogwarts')
print(f"这是set7",set7, type(set7))
set7.update([1, 2, 3])
print(f"这是set7",set7, type(set7))
'''3、remove方法：remove(item)'''
# 1、元素存在
set8 = {1, 2, 'hogwarts'}
set8.remove(1)
print(f"这是set8",set8)
# 2、元素不存在会报错
# set8.remove(100)

'''4、discard方法：discard(item)'''
# 1、元素存在
set8.discard(1)
print(f"这是set8",set8)
# # 2、元素不存在
# set8.discard(100)

'''5、pop方法：pop()'''
set9 = {1, 2, 'hogwarts'}
set9.pop()
print(f"这是set9",set9)
'''6、clear方法：clear()'''
set10 = {1, 2, 3, 4, 5}
set10.clear()
print(f"这是set10",set10)

"""集合运算"""
a = {1, 3, 2}
b = {5, 1, 4}
# 1、交集运算 intersection &
print(f"交集运算1",a.intersection(b))
print(f"交集运算1",a & b)
# 2、并集运算 union或|
print(f"并集运算1",a.union(b))
print(f"并集运算2",a | b)

# 3、差集运算 difference或-号
print(f"差集运算1",a.difference(b))
print(f"差集运算2",a - b)

"""
集合推导式 
实例：寻找hogwartsss 与 hello world 的共相同字母
"""
set10 = set()
for s in 'hogwartsss':
    if s in 'hello world':
        set10.add(s)
print(f"集合推导式1",set10)

set11 = {s for s in 'hogwartsss' if s in 'hello world'}
print(f"集合推导式2",set11)