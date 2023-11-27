import os
help(os)  # 查看os模块说明文档
print(dir(os))  #查看os模块的属性和方法

"""第1部分：os 操作系统相关"""

print(os.name)  # 获取系统名称

print(os.environ)  # 获取系统环境变量信息

print(os.getenv('PATH'))  # 获取指定名称的环境变量信息

os.system('pwd')  # 执行系统指令


"""第2部分：os 目录相关"""

print(os.getcwd())  # 获取当前所在目录

os.chdir('..')  # 切换目录
print(os.getcwd())

print(os.listdir())  # 列出当前目录下的所有文件

os.mkdir('demo')  # 创建空目录

os.makedirs('a/b/c')  # 递归创建多级空目录

os.rmdir('demo')  # 删除空目录
os.rmdir('a')

os.rename('demo', 'hello')  # 重命名目录

os.remove('world.txt')  # 删除文件



"""第3部分：os 路径相关"""

print(os.path.abspath("./os_demo.py"))  # 返回绝对路径

print(os.path.basename("/Users/xiaofo/coding/pythonProject/course/os_demo.py"))  # 返回文件名

print(os.path.dirname("/Users/xiaofo/coding/pythonProject/course/os_demo.py"))  # 返回文件路径

print(os.path.split("/Users/xiaofo/coding/pythonProject/course/os_demo.py"))  # 分割路径

print(os.path.join("/Users/xiaofo/coding/pythonProject/course", "os_demo.py"))  # 拼接路径

print(os.path.exists("/Users/xiaofo/coding/pythonProject/course/os_demo.py"))  # 判断路径是否存在
print(os.path.exists("./os_demo.py"))
print(os.path.exists("./os_demo2.py"))

print(os.path.isdir("/Users/xiaofo/coding/pythonProject/course"))  # 判断是否是目录
print(os.path.isdir("/Users/xiaofo/coding/pythonProject/course/os_demo.py"))

print(os.path.isfile("/Users/xiaofo/coding/pythonProject/course/os_demo.py"))  # 判断是否是文件
print(os.path.isfile("/Users/xiaofo/coding/pythonProject/course"))

print(os.path.getsize("/Users/xiaofo/coding/pythonProject/course/os_demo.py"))  # 获取文件大小
