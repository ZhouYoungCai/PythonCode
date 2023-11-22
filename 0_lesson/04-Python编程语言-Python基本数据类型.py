01、python基本数据类型与操作
    1.变量：是一种存储数据的载体。计算机中的变量是实际存在的数据或者说是存储器中的存储数据的一块内存空间。
	      变量的值是可以读取和修改的。
		  变量命名规则：
		      变量名是由字母（广义的Unicode字符，不包括特殊字符）、数字和下划线构成，数字不能开头
			  大小写敏感
			  不要跟关键字
	2.数字：常用数字类型：int、float
	     常用运算符：赋值  =
		             加减乘除    + - * /
					 取余 %
					 乘方  **
					 修改运算优先级  （）
					 等于  ==  正确返回true，错误返回false
					 不等于  ！=   正确返回true，错误返回false
			int整型：int_a = 1  type(int_a)
			float浮点型float_a = 1  type(float_a)
	3.字符串：
	       \:转义符   \n  换行
			   str_a = "abc"
			   print(str_a)
			   print(type(str_a))
			   str_a = "abc53424t34\n53455345534"  #\n  换行
			   print(str_a)
			   str_a = "abc53424t34\\n53455345534"  #\n  换行,多加一个斜杠，就可以打印\n
		   r：忽略转义符的作用
				str_a = r"abc53424t34\\n53455345534"  #\n  换行,前面加r，就可以打印\n，用法同上
		   +：多个字符串连接
				str_a="123a"
				str_b="456b"
				print(str_a+str_b)
		   索引
				字符串：abcdefg
			  对应索引：0123456
			  str_a = "abcdefg"
			  print(str_a[0])
		   切片
				str_a = "abcdefg"
				print(str_a[1:5])  #打印2~6位
				print(str_a[1:])   #打印2~最后位，步长默认为1
				print(str_a[1:5:2])  #打印2~6位,步长为2
	4.列表：中括号[]    #列表的索引和切片和字符串的索引和切片一样，遵循前闭后开原则1<=X<5
		定义:使用中括号包起来的元素就叫做列表
			var_list = [1,2,3,4,5,"a","b","c",True]
			print(var_list)
		索引
			print(var_list[1])  #拿第2个数据2
			print(var_list[-1])  #拿最后一个数据True
		切片
			var_list = [1,2,3,4,5,"a","b","c",True]
			print(var_list[1:5])  #打印2~6位
			print(var_list[1:])   #打印2~最后位，步长默认为1
			print(var_list[1:5:2])  #打印2~6位,步长为2