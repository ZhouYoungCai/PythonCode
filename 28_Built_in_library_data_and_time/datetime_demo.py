"""
__author__ = 'hogwarts_xixi'
"""
import datetime

nowtime = datetime.datetime.now()   #当前日期时间
print(nowtime)
print(nowtime.day)
print(nowtime.month)
print(nowtime.year)

print(nowtime.timestamp())   # 转成时间戳

print(datetime.datetime(2021, 10, 10))

s = "2021-09-27 06:47:06"

s1 = datetime.datetime.strptime(s, '%Y-%m-%d %H:%M:%S')   # 将字符串 转换为datetime实例
print(s1)
print(type(s1))

result = s1.strftime('%a  %b  %d %H:%M')   # 时间转成字符串
print(result)
mtimestamp = 1632725226.129461

s = datetime.datetime.fromtimestamp(mtimestamp)  #时间戳-> 时间
print(s)

print(s.timestamp())  # 将时间->时间戳