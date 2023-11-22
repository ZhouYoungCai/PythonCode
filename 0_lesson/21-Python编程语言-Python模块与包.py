1、安装mypy：pip install mypy
    安装后可以检查编码的语法错误
2、类型注解总结
    增强代码可读性
	ide中代码提示
	静态代码检查
3、什么是模块？
   包含Python定义和语句的文件
   .py文件
   作为脚本运行
4、模块导入
    import 模块名
	from 模块名 import 方法/变量/类
	from 模块名 import *
	注意：
	    同一个模块写多次，只被导入一次
		import应该放在代码的顶端
5、模块分类
    系统内置模块
	第三方开源模块
	自定义模块
6、系统内置模块
    import sys
	import os
	import re  正则表达式
	import time
	import json
	导入了未使用就会置灰，使用了就会变成绿色、
7、第三方开源模块
    是通过包管理工具pip完成的，或者IDE里面通过python interpreter安装
	import pyyaml
	from pyyaml import *
8、常用方法
    dir() 找出当前模块定义的对象
	dir(sys) 找出参数模块定义的对象
9、使用模块的总结
    代码的可维护性
	提升编码效率
	函数名可重复（起名避免与系统重复）