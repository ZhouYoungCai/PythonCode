01、yaml介绍
    一种数据序列化格式
	用于人类的可读性和与脚本语言的交互
	一种被认为可以超越xml、json的配置文件
02、yaml基本语法规则
    大小写敏感
	使用缩进表示层级关系
	缩进时不允许使用tab键，只允许使用空格
	缩进的空格数目不重要，只要相同层级的元素左侧对其即可
	#表示注释，从这个字符一直到行尾，都会被解析器忽略
03、yaml支持的数据结构
    对象：键值对的集合，用冒号“：”表示
	数组：一组按次序排列的值，前面加“-”
	纯量：单个的、不可再分的值
	    字符串
		布尔值
		整数
		浮点数
		Null
		时间
		日期
04、安装pyyaml
    python的yaml解析器和生成器
	官网：https://pypi.org/project/PyYaml/
	安装命令：pip install pyyaml
	使用：import yaml/from yaml import *
05、创建yaml文件，读yaml文件