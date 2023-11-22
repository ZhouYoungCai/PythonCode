01、python中处理时间的模块
    time
	datetime
	calendar
02、常见的时间表示形式
    时间戳
	格式化的时间字符串
03、datetime常用的类
    datetime（from datetime import datetime）时间日期相关
	timedelta（from datetime import timedelta）计算两个时间的时间差
	timezone（from datetime import timezone） 时区相关
    
	import datetime  #导入时间包
	nowtime = datetime.datetime.now()  #构建对象
	print(nowtime)  #打印当前时间