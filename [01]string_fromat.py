# 01、python字符串的基本操作
#     字符串操作的使用场景：数据提取之后的通用格式：日志，excel
# 	                      第三方数据信息
# 02、字符串的定义
# 	#单行字符串
# 	str_a = "string"
# 	#多行字符串
# 	str_a = """
# 	string
# 	safdfsdfsfsfsfsdfdsfsf
# 	"""
# 03、字符串的特殊字符
# 	\n   换行    打印换行，例如：print("hogwarts \n 测试学院")
# 	\    转义符  打印有特殊含义的字符，例如：print("hogwarts \\n 测试学院")
# 04、字符串格式化符号：
# 	    %c:格式化字符及其ASCII码
# 		%s:格式化字符串
# 		%d:格式化整数
# 		%u:格式化无符号整型
# 		%o:格式化无符号八进制数
# 		%x:格式化无符号十六进制数
# 		%X:格式化无符号十六进制数（大写）
# 		%f:格式化浮点数字，可指定小数点后的精度
# 		%e:用科学计数法格式化浮点数
# 		%p:用十六进制数格式化变量的地址
# 	replace 替换
# 	strip  去除字符串前后的空格
# 	例如：print("hogwarts teacher is %s"%"张家辉")
# 05、字符串之字面量插值
# 	"str".format()
# 		#不设置指定位置，按默认顺序
# 		"{} {}".format( "hogwarts","ad")
# 		#设置指定位置
# 		"{0} {1}".format("hogwarts","ad")
# 		#通过名称传递变量
# 		"{name}测试开发".format(name="霍格沃兹")
# 	代码：
# 		demo = "hogwarts is a {}"  #demo是原始的变量内容
# 		demo_res = demo.format("school")  #demo_res是替换过后的变量内容
# 		print(demo_res)
# 	代码：
# 		demo = "hogwarts is a {0} {1}"  #demo是原始的变量内容,1和0的位置可以换
# 		demo_res = demo.format("very good","school")  #demo_res是替换过后的变量内容
# 		print(demo_res)
# 	使用关键字传递参数：
# 		demo = "hogwarts is a {school}"  #demo是原始的变量内容
# 		demo_res = demo.format(school="very good")  #demo_res是替换过后的变量内容
# 		print(demo_res)   #打印结果：hogwarts is a very good
# 	最优雅的方式(常用)：
# 		name = "Bob"
# 		school = "hogwarts"
# 		print(f"我的名字叫做{name}，毕业于{school}")   #通过 f"(变量名)，f的意思是format
# 06、字符串常用api之join
# 	把列表转换为字符串join
# 	代码：
# 		a = ["h","o","g","w","a","r","t","s"]
# 		print("".join(a))
#07、字符串常用操作之切分操作
#根据split内容将字符串进行切分
# demo = "hogwarts school"
# print(demo.split(" "))  #冒号中间是空格，就是以空格作为切分
# 08、字符串常用API之replace
# replace:将目标字符串替换成想要的字符串
# 例如将school替换为top school：
print("hogwarts school".replace("school","top school"))
a = "my name is aaa"
print(a.replace("aaa","张家辉"))

