01、JSON
	JSON 是用于存储和交换数据的语法，是一种轻量级的数据交换格式。
	使用场景
	接口数据传输
	序列化
	配置文件
02、JSON 结构
	键值对形式
	数组形式
03、json 库
	可以从字符串或文件中解析 JSON
	该库解析 JSON 后将其转为 Python 字典或者列表
04、常用方法
	dumps()：将 Python 对象编码成 JSON 字符串
	loads()：解码 JSON 数据，该函数返回 Python 对象
	dump()： Python 对象编码，并将数据写入 json 文件中
	load()：从 json 文件中读取数据并解码为 Python 对象
	import json

	# 定义 python 结构
	data = [{'a': 1, 'b': '2', 'c': True, 'd': False, 'e': None }]   

	# 将 python 对象编码为 JSON 字符串
	json_data = json.dumps(data)
	# 将 JSON 字符串解码为 python 对象
	python_data = json.loads(json_data)
	# 写入 JSON 数据，在代码当前目录生成一个 data.json 的文件
	with open('data.json', 'w') as f:    
		 json.dump(data, f)   
	# 读取数据，读取 json 文件并解码成 python 对象
	with open('data.json', 'r') as f:
		 data = json.load(f)
05、dumps 常用参数
	indent：根据数据格式缩进显示，默认为 None，没有缩进
	ensure_ascii：对中文使用 ASCII 编码，默认为 True
	import json

	data = {
		'a': 1, 
		'b': '霍格沃兹', 
		'c': True, 
		'd': False, 
		'e': None }

	python_data = json.dumps(data, indent=4, ensure_ascii=False)
	print(python_data)
06、pycharm快速注释和取消注释
    CTRL+/