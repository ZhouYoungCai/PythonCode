# help(sys)
# print(dir(sys))
import os.path  # 添加自定义路径到导包路径列表中
import sys
#from path_demo import hello
"""sys模块常用方法"""

print(sys.version)  # 返回 Python 解释器版本
print(sys.platform)  # 返回操作系统平台名称
print(sys.modules)  # 返回已导入的模块信息  # 返回外部向程序传递的参数
print(sys.modules.keys())
print(sys.path)  # 返回导包的搜索路径列表

my_dir = os.path.dirname(os.path.abspath(__file__)) + "/hello"
sys.path.append(my_dir)

hello()
print(sys.path)

"""sys模块常用方法"""

print(sys.getdefaultencoding())  # 获取系统当前编码


sys.exit()  # 运行时退出
sys.exit(0)
sys.exit("error")

import time
for i in range(10):
    if i == 6:
        print("exit...")
        sys.exit("正常退出了")
    print(f'running{i}...')
    time.sleep(1)
