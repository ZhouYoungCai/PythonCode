# 01、python的运算符
#     python基础语法的内容
# 	通常表示不同数据或变量之间的关系
# 	算数运算符：加、减、乘、除、取余、幂、整除
# 	比较运算符：==、！=、>、<、>=、<=
# 	赋值运算符：=   +=   -=   *=   /=   %=  **=   //=   例如：a = a+2   ==  a += 2   左右两边相等
# 	逻辑运算符： and   or    not
# 	成员运算符：in      not in
#     身份运算符：is   、 is not
# 02、运算符的作用
# 	Python基础语法的内容
# 	通常表示不同数据或变量之间的关系
# 03、算数运算符
# 	运算符	描述
# 	+	加
# 	-	减
# 	*	乘
# 	/	除
# 	%	取模
# 	**	幂
# 	//	取整除
# 	# 加
# 	a = 1+1
# 	# 减
# 	b = 2-1
# 	#变量之间也可以做运算
# 	c = 4
# 	d = 3
# 	e = c-d
# 	# 乘
# 	f = 1*2
# 	# 除
# 	g = 3/2
# 	# 取模（取余）
# 	h = 5%2
# 	# 幂
# 	i = 2**3
# 	# 取整除
# 	j = 3//2
# 04、比较运算符，输出的结果是布尔值：true false
# 	运算符	描述
# 	==	等于
# 	!=	不等于
# 	>	大于
# 	<	小于
# 	>=	大于等于
# 	<=	小于等于
a = 1
b = 2
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a<=b)
print(a>=b)
# 05、赋值运算符
# 	运算符	描述
# 	=	简单赋值运算符
# 	+=	加法赋值运算符
# 	-=	减法赋值运算符
# 	*=	乘法赋值运算符
# 	/=	除法赋值运算符
# 	%=	取模赋值运算符
# 	**=	幂赋值运算符
# 	//=	取整赋值运算符
# 	# 简单赋值
# 	a = 1
# 	# 多个变量赋值
# 	a,b = 1,2
# 	# 加法运算
# 	# a = a+1
# 	# 加法赋值运算
# 	a += 1
# 06、逻辑运算符
# 	运算符	逻辑表达式	描述
# 	and	x and y	x、y 都为真才为真，有一个为假即为假
# 	or	x or y	x、y 有一个为真即为真，都为假为假
# 	not	not x	如果 x 为假，则not x为真
# 	a, b= True, False
# 	print(a and b)
# 	print(a or b)
# 	print(not a)
# 	print(not b)
# 07、成员运算符
# 	运算符	描述
# 	in	如果在指定的序列中找到值返回 True，否则返回 False。
# 	not in	如果在指定的序列中没有找到值返回 True，否则返回 False。
# 	list_a = ["a", "b", "c"]
# 	str_a = "abcde"
# 	str_b = "bcde"
#
# 	print("a" in list_a)
# 	print("a" not in list_a)
# 	print("a" in str_a)
# 	print("a" not in str_a)
# 	print("a" in str_b)
# 08、身份运算符
# 	运算符	描述
# 	is	is 是判断两个标识符是不是引用自一个对象
# 	is not	is not 是判断两个标识符是不是引用自不同对象
# 	list_a = ["a", "b", "c"]
# 	list_b = ["a", "b", "c"]
#
# 	print(id(list_a)) # 使用id查看变量的内存地址
# 	print(id(list_b))
# 	print(list_a is list_b)
# 	print(list_a == list_b)
