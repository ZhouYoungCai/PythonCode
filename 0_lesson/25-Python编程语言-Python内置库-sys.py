01、sys 概述
	是 Python 自带的内置模块
	是与 Python 解释器交互的桥梁
02、sys 使用
	常用属性

	常用方法

	导入 sys 模块

	# 导入sys模块
	import sys

	# 查看sys模块帮助文档
	help(sys)

	# 查看sys模块的属性和方法
	print(dir(sys))
03、sys 常用属性
	sys.version：返回 Python 解释器版本
	sys.platform：返回操作系统平台名称
	sys.argv：返回外部向程序传递的参数
	sys.modules：返回已导入的模块信息
	sys.path：返回导包的搜索路径列表
	"""sys模块常用属性"""
	# 返回Python 解释器版本
	print(sys.version)
	# 返回操作系统平台名称
	print(sys.platform)
	# 返回外部向程序传递的参数
	print(sys.argv)
	# 返回已导入的模块信息
	print(sys.modules)
	print(sys.modules.keys())
	# 返回导包的搜索路径列表
	print(sys.path)
04、sys 常用方法
	sys.getdefaultencoding()：获取编码方式

	sys.exit()：运行时退出

	"""sys模块常用方法"""
	# 获取系统当前编码
	print(sys.getdefaultencoding())

	# 运行时退出
	sys.exit()