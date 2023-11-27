#coding:utf-8
import os

"""第1部分：os 操作系统相关"""

print(os.name)  # 获取系统名称

print(os.environ)  # 获取系统环境变量信息

print(os.getenv('PATH'))  # 获取指定名称的环境变量信息

os.system('pwd')  # 执行系统指令