1、os 概述
	os: Operating System
	os 模块的常用功能
	跨平台的差异
2、os 使用
	导入 os 模块
	查看 os 模块使用文档
	help(os)
	dir(os)
	import os

	# 查看os模块说明文档
	help(os)

	# 查看os模块的属性和方法
	print(dir(os))
3、os 常用方法
	系统相关
	操作目录
	操作路径
4、os 操作系统相关
	os.name：获取系统名称
	os.environ：获取系统环境变量信息
	os.getenv(‘PATH’)：获取指定名称的环境变量信息
	os.system()：执行系统指令
	import os

	# os.name：获取系统名称 nt代表window，posix代表linux
	print(os.name)

	# os.environ：获取系统环境变量信息
	print(os.environ)

	# os.getenv('PATH')：获取指定名称的环境变量信息
	print(os.getenv('PATH'))

	# os.system()：执行系统指令
	os.system('pwd')  # linux系统
	print(os.system('dir'))  # windows系统
5、os 目录相关
	os.getcwd()：获取当前目录
	os.chdir()：切换目录
	os.listdir()：列出当前目录内容
	os.mkdir()：创建空目录
	os.makedirs()：递归创建多级目录
	os.rmdir()：删除空目录
	os.rename()：重命名目录
	os.remove()：删除文件
	"""目录相关"""
	# 获取当前所在目录 get current directory
	print(os.getcwd())
	# 切换目录 change directory
	os.chdir('..')
	# 列出当前目录下的所有文件
	print(os.listdir())
	# 创建空目录
	os.mkdir('new')
	# 递归创建多级空目录
	os.makedirs('a/b/c')
	# 删除空目录
	os.rmdir('new')
	# 重命名目录
	os.rename('a', 'a1')
	# 删除文件
	os.remove('demo.txt')
6、os 路径相关
	path方法	            说明
	os.path.abspath(path)	返回绝对路径
	os.path.basename(path)	返回文件名
	os.path.dirname(path)	返回文件路径
	os.path.split(path)	    分割路径
	os.path.join(path)	    拼接路径
	os.path.exists(path)	判断路径是否存在
	os.path.isdir(path)	    判断是否是目录
	os.path.isfile(path)	判断是否是文件
	os.path.getsize(path)	获取文件大小
7、os 路径用法实例
	# 返回绝对路径
	print(os.path.abspath("./os_demo.py"))
	# 返回文件名
	print(os.path.basename("/Users/xiaofo/coding/pythonProject/course/os_demo.py"))
	# 返回文件路径
	print(os.path.dirname("/Users/xiaofo/coding/pythonProject/course/os_demo.py"))
	# 分割路径
	print(os.path.split("/Users/xiaofo/coding/pythonProject/course/os_demo.py"))
	# 拼接路径
	print(os.path.join("/Users/xiaofo/coding/pythonProject/course", "os_demo.py"))
	# 判断路径是否存在
	print(os.path.exists("/Users/xiaofo/coding/pythonProject/course/os_demo.py"))
	print(os.path.exists("./os_demo.py"))
	# 判断是否是目录
	print(os.path.isdir("../demos"))
	# 判断是否是文件
	print(os.path.isfile("./hello.py"))
	# 获取文件大小
	print(os.path.getsize("/Users/xiaofo/coding/pythonProject/course/os_demo.py"))