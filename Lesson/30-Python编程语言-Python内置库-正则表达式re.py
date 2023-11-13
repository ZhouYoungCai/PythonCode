01、目录
	正则表达式
	使用 re 模块实现正则表达式操作
02、什么是正则表达式
	正则表达式就是记录文本规则的代码
	可以查找操作符合某些复杂规则的字符串
03、使用场景
	在 python 中使用正则表达式
	处理字符串
	处理日志
	把正则表达式作为模式字符串
	正则表达式可以使用原生字符串来表示
	原生字符串需要在字符串前方加上 r'string'
	# 匹配字符串是否以 hogwarts_ 开头

	r'hogwart_\w+'
04、正则表达式对象转换
	compile()：将字符串转换为正则表达式对象
	需要多次使用这个正则表达式的场景
	import re

	'''
	prog：正则对象，可以直接调用匹配、替换、分割的方法，不需要再传入正则表达式
	pattern：正则表达式
	'''

	prog = re.compile(pattern)
05、匹配字符串
	match()：从字符串的开始处进行匹配
	search()：在整个字符串中搜索第一个匹配的值
	findall()：在整个字符串中搜索所有符合正则表达式的字符串，返回列表
	import re

	'''
	pattern: 正则表达式
	string: 要匹配的字符串
	flags: 可选，控制匹配方式
		- A：只进行 ASCII 匹配
		- I：不区分大小写
		- M：将 ^ 和 $ 用于包括整个字符串的开始和结尾的每一行
		- S：使用 (.) 字符匹配所有字符（包括换行符）
		- X：忽略模式字符串中未转义的空格和注释
	'''

	re.match(pattern, string, [flags])
	re.search(pattern, string, [flags])
	re.findall(pattern, string, [flags])
06、替换字符串
	sub()：实现字符串替换
	import re

	'''
	pattern：正则表达式
	repl：要替换的字符串
	string：要被查找替换的原始字符串
	count：可选，表示替换的最大次数，默认值为 0，表示替换所有匹配
	flags：可选，控制匹配方式
	'''

	re.sub(pattern, repl, string, [count], [flags])
07、分割字符串
	split()：根据正则表达式分割字符串，返回列表
	import re

	'''
	pattern：正则表达式
	string：要匹配的字符串
	maxsplit：可选，表示最大拆分次数
	flags：可选，控制匹配方式
	'''

	re.split(pattern, string, [maxsplit], [flags])
	本课程版权归『霍格沃兹测试开发』所有，仅限个人学习使用，严禁任何形式的录制、传播和账号分享。
	一经发现，平台有权做封号处理，情节严重者将承担法律责任。