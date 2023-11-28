# -*- coding: utf-8 -*-
# @Author : feier
# @File : json_demo.py

import json


data = {  # 定义 python 结构
    'a': 1,
    'b': ['2', '3'],
    'c': True,
    'd': False,
    'e': None
}

json_data = json.dumps(data)  # 将 python 对象编码为 JSON 字符串
print(json_data)


json_data = '''{"a": 1, "b": ["2", "3"], "c": true, "d": false, "e": null}'''  #定义 JSON 字符串

python_data = json.loads(json_data)   # 将 JSON 字符串转化为 python 对象
print(python_data)
print(type(python_data))


with open('data.json', 'w') as f:  # 把 python 对象转化为 JSON 格式的数据并且写入 JSON 文件
    json.dump(data, f)


with open('data.json','r') as f:   # 读取 JSON 文件，并且转化为 python 对象
    data = json.load(f)
    print(data)
    print(type(data))

# 定义 python 结构
data = {
    'a': 1,
    'b': '霍格沃兹',
    'c': True,
    'd': False,
    'e': None
}


json_data = json.dumps(data, ensure_ascii=False, indent=4)  # 转化成为 JSON 格式
print(json_data)