01、字典定义与使用
	字典是无序的键值对集合
	字典用大括号{}包围
	每个键/值对之间用一个逗号分隔
	各个键与值之间用一个冒号分隔
	字典是动态的
	字典常用方法
	字典推导式
	实例
02、字典使用：创建
	创建字典
	使用大括号填充键值对
	通过构造方法 dict()
	使用字典推导式
	"""字典使用：创建"""
	# 1、使用大括号填充键值对
	dc = {'name': 'Harry Potter', 'age': 18}
	print(type(dc), dc)

	# 2、使用字典构造方法
	dc1 = dict()  # 空字典
	dc2 = dict(name="Harry Potter", age=18)  # 关键字参数赋值
	print(type(dc2), dc2)
	dc3 = dict([("name", "Harry Potter"), ("age", 18)])
	print(type(dc3), dc3)

	# 3、使用字典推导式
	dc4 = {k: v for k, v in [("name", "Harry Potter"), ("age", 18)]}
	print(type(dc4), dc4)
03、字典使用：访问元素
	访问元素
	与字典也支持中括号记法[key]。
	字典使用键来访问其关联的值。
	访问时对应的 key 必须要存在
	"""字典使用：访问元素"""
	dc = {"name": "Harry Potter", "age": 18}
	# 1、访问存在的key
	print(dc["name"])
	print(dc["age"])

	# 2、访问不存在的key，会报KeyError错误
	print(dc['hobby'])
04、字典使用：操作元素
	语法：dict[key] = value
	添加元素
	键不存在
	修改元素
	键已经存在
	"""字典使用：操作元素"""
	dc = {"name": "Harry Potter", "age": 18}
	# 1、修改年龄，改为20
	dc['age'] = 20
	print(dc)

	# 2、新增hobby字段
	dc['hobby'] = 'Magic'
	print(dc)
05、字典使用：嵌套字典
	嵌套字典

	字典的值可以是字典对象

	"""字典使用：嵌套字典"""
	dc = {"name": "Harry Potter", "age": 18, "course": {"magic": 90, "python": 80}}
	# 1、获取课程Magic的值
	print(dc['course']['magic'])

	# 2、把python分数改成100分
	dc['course']['python'] = 100
	print(dc)
06、字典方法
	keys()
	values()
	items()
	get()
	update()
	pop()
07、字典方法 keys()
	keys()

	返回由字典键组成的一个新视图对象。

	入参：无

	"""字典方法 keys()"""
	dc = {"name": "Harry Potter", "age": 18}
	keys = dc.keys()
	print(type(keys), keys)

	# 1、遍历查看所有的键
	for key in keys:
		print(key)

	# 2、将视图对象转成列表
	print(list(keys))
08、字典方法 values()
	values()

	返回由字典值组成的一个新视图对象。

	"""字典方法 values()"""
	dc = {"name": "Harry Potter", "age": 18}
	values = dc.values()
	print(type(values), values)

	# 1、遍历查看所有的值
	for value in values:
		print(value)

	# 2、将视图对象转成列表
	print(list(values))
09、字典方法 items()
	items()

	返回由字典项 ((键, 值) 对) 组成的一个新视图对象。

	"""字典方法 items()"""
	dc = {"name": "Harry Potter", "age": 18}
	items = dc.items()
	print(type(items), items)

	# 1、遍历查看所有的项
	for item in items:
		print(item)

	# 2、将视图对象转成列表
	print(list(items))
10、字典方法 get()
	get(key)

	获取指定 key 关联的 value 值。

	入参：

	key：字典的键，必传。
	返回：

	如果 key 存在于字典中，返回 key 关联的 value 值。
	如果 key 不存在，则返回 None。
	此方法的好处是无需担心 key 是否存在，永远都不会引发 KeyError 错误。

	"""字典方法 pop()"""
	dc = {"name": "Harry Potter", "age": 18}

	# 1、访问存在的key
	name = dc['name']
	print(name)

	# 2、访问不存在的key
	hobby = dc.get('hobby')
	print(hobby)
11、字典方法 update()
	update(dict)

	使用来自 dict 的键/值对更新字典，覆盖原有的键和值。

	入参：

	dc：字典对象，必传
	返回：None

	dc = {"name": "Harry Potter", "age": 18}
	dc.update({"age": 20, "hobby": "magic"})
	print(dc)
12、字典方法 pop()
	pop(key)

	删除指定 key 的键值对，并返回对应 value 值。

	入参：

	key：必传
	返回：

	如果 key 存在于字典中，则将其移除并返回 value 值
	如果 key 不存在于字典中，则会引发 KeyError。
	"""字典方法 pop()"""
	dc = {"name": "Harry Potter", "age": 18}

	# 1、弹出
	item = dc.pop("age")
	print(dc, item)

	# 2、删除不存在的key
	# dc.pop("hobby")  # 报错keyError
13、字典推导式
	字典推导式：可以从任何以键值对作为元素的可迭代对象中构建出字典。

	实例：给定一个字典对象{'a': 1, 'b': 2, 'c': 3}，找出其中所有大于 1 的键值对，同时 value 值进行平方运算。

	# 未使用字典推导式的写法
	dc = {'a': 1, 'b': 2, 'c': 3}
	d_old = dict()
	for k, v in dc.items():
		if v > 1:
			d_old[k] = v ** 2
	print(d_old)

	# 使用字典推导式
	d_new = {k : v ** 2 for k,v in dc.items() if v > 1 }
	print(d_new)	
14、实例
	"""
	给定一个字典对象，请使用字典推导式，将它的key和value分别进行交换。也就是key变成值，值变成key。

	输入: {'a': 1, 'b': 2, 'c': 3}
	输出: {1: 'a', 2: 'b', 3: 'c'}
	"""			