"""
__author__ = 'hogwarts_xixi'
"""
import datetime

now = datetime.datetime.now()  # 时间格式

c_time = now.strftime("%Y%m%d_%H%M%S")  # 转成字符串
print(c_time)

log_name = c_time+'.log'
with open(log_name, 'w+',encoding='utf-8') as f :
    # datetime [level] line: 13 this is a log message
    message = f"{now} [info] line: 14 this is a log message"
    f.write(message)