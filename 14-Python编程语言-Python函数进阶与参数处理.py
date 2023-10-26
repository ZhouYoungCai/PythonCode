01、可变参数
	可变参数也称为不定长参数
	传入函数中实际参数可以是任意多个
	常见形式
	*args
	**kwargs
02、*args
	接收任意多个实际参数，并将其放到一个元组中
	使用已经存在的列表或元组作为函数的可变参数，可以在列表的名称前加*
	def print_language(*args):
		print(args)

	print_language("python", "java", "php", "go")

	params = ["python", "java", "php", "go"]
	print_language(*params)
03、**kwargs
	接收任意多个类似关键字参数一样显式赋值的实际参数，并将其放到一个字典中
	使用已经存在字典作为函数的可变参数，可以在字典的名称前加**
	def print_info(**kwargs):
		print(kwargs)

	print_info(Tom=18, Jim=20, Lily=12)

	params = {'Tom':18, 'Jim':20, 'Lily':12}
	print_language(**params)