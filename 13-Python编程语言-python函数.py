01、目录
	函数的作用
	函数定义
	函数调用
	参数传递
	函数返回值
02、函数的作用
	函数是组织好的，可重复使用的，用来实现单一或相关联功能的代码段
	函数能提高应用的模块性和代码的重复利用率
	python 内置函数：https://docs.python.org/zh-cn/3.8/library/functions.html
03、函数定义
	def：函数定义关键词
	function_name：函数名称
	()：参数列表放置的位置，可以为空
	parameter_list：可选，指定向函数中传递的参数
	comments：可选，为函数指定注释
	function_body：可选，指定函数体
	def function_name([parameter_list]):
		[''' comments ''']
		[function_body]
04、定义函数的注意事项：
		缩进：python 是通过严格的缩进来判断代码块儿
		函数体和注释相对于 def 关键字必须保持一定的缩进，一般都是 4 个空格
		pycharm 自动格式化快捷键：ctrl+alt+L
		定义空函数
		使用 pass 语句占位
		写函数注释 comments
05、函数调用
	function_name：函数名称
	parameter_value：可选，指定各个参数的值
	function_name([parameter_value])
06、参数传递
	形式参数：定义函数时，函数名称后面括号中的参数
	实际参数：调用函数时，函数名称后面括号中的参数
	# a, b, c 为形式参数
	def demo_func(a, b, c):
		print(a, b, c)

	# 1, 2, 3 为实际参数
	demo_func(1, 2, 3)
07、位置参数
	数量必须与定义时一致
	位置必须与定义时一致
	def demo_func(a, b, c):
		print(a, b, c)

	# 1 赋值给 a, 2 赋值给 b, 3 赋值给 c
	demo_func(1, 2, 3)
08、关键字参数
	使用形式参数的名字确定输入的参数值
	不需要与形式参数的位置完全一致
	def demo_func(a, b, c):
		print(a, b, c)

	demo_func(a=1, b=2, c=3)
09、为参数设置默认值
	定义函数时可以指定形式参数的默认值
	指定默认值的形式参数必须放在所有参数的最后，否则会产生语法错误
	param=default_value：可选，指定参数并且为该参数设置默认值为 default_value
	def function_name(..., [param=default_value]):
		[function_body]
10、函数返回值
	- value：可选，指定要返回的值

	def function_name([parameter_list]):
		[''' comments ''']
		[function_body]
		return [value]
11、课后练习
    自定义一个函数，并调用