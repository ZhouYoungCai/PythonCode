01、set集合
    集合定义与使用
	    无序的唯一对象集合
		用大括号{}包围，对象相互之间使用逗号分隔
		集合是动态的，可以随时添加或删除元素
		集合是异构的，可以包含不同类型的数据
	集合常用方法：clear、add、update、remove、discard、pop
	              交集运算intersection（）、并集运算union（）、差集运算difference（）
	集合推导式；
	类似列表推导式，同样集合支持集合推导式
    语法：{x for x in ... if ...}
    # 使用推导式生成集合
    """集合推导式"""
	# 使用推导式生成集合
	st = {x for x in 'hogwarts' if x in 'hello world'}
	print(st)
02、Set 集合
	集合定义与使用
	集合常用方法
	集合推导式
03、Set 集合
	集合定义与使用
	集合常用方法
	集合推导式
04、集合使用：创建
	创建
	通过使用{}填充元素
	通过构造方法 set()
	通过集合推导式
	"""创建集合"""
	# 1、使用大括号{}填充元素
	st4 = {1, 2, 3}
	st5 = {'a', 'b', 'c'}

	# 2、使用构造方法创建集合
	st1 = set()  # 空集合
	st2 = set('hogwarts')

	li = [1, 1, 2, 2, 3, 3]
	st3 = set(li)


	# 3、使用集合推导式
	st6 = {x for x in li}

	# 注意：不要单独使用{ }来创建空集合
	st7 = {}  # 这是字典类型
	print(type(st7))
05、集合使用：成员检测
	in
	判断元素是否在集合中存在
	not in
	判断元素是否在集合中不存在
	"""集合使用：成员检测"""
	st = {1, 2, 3, 4, 5}
	# in
	print(2 in st)

	# not in
	print(99 not in st)
06、集合方法
	add()
	update()
	remove()
	discard()
	pop()
	clear()
07、集合方法 add()
	add(item)：将单个对象添加到集合中
	入参：对象 item
	返回：None
	"""集合方法 add()"""
	# 添加元素
	st = {1, 2, 3}
	st.add(99)
	st.add('hogwarts')
08、集合方法 update()
	update(iterable)

	批量添加来自可迭代对象中的所有元素

	入参：可迭代对象 iterable

	返回：None

	"""集合方法 update()"""
	li = [1, 2, 3]
	tup = (2, 3, 4)
	st = {'a', 'b', 'c'}

	# 1、批量添加列表中的元素
	st1 = set()
	st1.update(li)
	# 2、批量添加元组中的元素
	st1.update(tup)
	# 3、批量添加集合中的元素
	st1.update(st)
	print(st1)
09、集合方法 remove()
	remove(item)：从集合中移除指定元素 item。
	入参：指定元素值
	返回：None
	如果 item 不存在于集合中则会引发 KeyError
	"""集合方法 remove()"""
	# 1、删除已存在的元素
	st = {1, 2, 3, 4, 5}
	st.remove(2)

	# 2、删除不存在的元素
	# st.remove(1024)  # KeyError
10、集合方法 discard()
	discard(item)：从集合中移除指定对象 item。
	入参：指定对象值
	返回：None
	元素 item 不存在没影响，不会抛出 KeyError 错误。
	"""集合方法 discard()"""
	# 1、删除已存在的元素
	st = {1, 2, 3, 4, 5}
	st.remove(2)

	# 2、删除不存在的元素
	st.discard(1024)
	print(st)
11、集合方法 pop()
	pop()：随机从集合中移除并返回一个元素。
	入参：无。
	返回：被移除的元组。
	如果集合为空则会引发 KeyError。
	"""集合方法 pop()"""

	# 1、随机删除某个对象
	st = {1, 2, 3, 4, 5}
	item = st.pop()
	print(item, st)

	# 2、集合本身为空会报错
	st = set()
	# st.pop()  # KeyError
12、集合方法 clear()
	clear()：清空集合，移除所有元素
	入参：无
	返回：None
	"""集合方法 clear()"""

	# 1、清空集合
	st = {1, 2, 3, 4, 5}
	st.clear()
13、集合运算
	交集运算
	并集运算
	差集运算
14、集合运算：交集
	交集运算

	intersection()

	操作符：&



	"""集合运算：交集"""

	# 交集运算
	set1 = {1, 3, 2}
	set2 = {2, 4, 3}
	print(set1.intersection(set2))
	print(set1 & set2)
15、集合运算：并集
	并集运算

	union()

	操作符：｜



	"""集合运算：并集"""

	# 求两个集合的并集
	set1 = {1, 3, 2}
	set2 = {2, 4, 3}
	print(set1.union(set2))
	print(set1 | set2)
16、集合运算：差集
	差集运算

	difference()

	操作符： -



	"""集合运算：差集"""
	# 集合求差集
	set1 = {1, 3, 2}
	set2 = {2, 4, 3}

	print(set1.difference(set2))
	print(set1 - set2)
17、集合推导式
	类似列表推导式，同样集合支持集合推导式
	语法：{x for x in ... if ...}
	# 使用推导式生成集合
	"""集合推导式"""
	# 使用推导式生成集合
	st = {x for x in 'hogwarts' if x in 'hello world'}
	print(st)