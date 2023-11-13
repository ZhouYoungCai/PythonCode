01、内置类装饰器
	不用实例化、直接调用
	提升代码的可读性
	内置装饰器	含义
	classmethod	类方法
	staticmethod	静态方法
02、普通方法
	定义：
	第一个参数为self，代表 实例本身
	调用：
	要有实例化的过程，通过 实例对象.方法名 调用
	# 1. 定义
	class MethodsDemo:
		param_a = 0 #类变量
		def normal_demo(self): # 定义一个类方法，第一个参数必须为self
			"""
			普通方法
			:return:
			"""
			print("这是一个普通方法", self.param_a)
	# 2. 调用
	md = MethodsDemo()
	md.normal_demo()
03、类方法
	定义：
	使用 @classmethod 装饰器，第一个参数为类本身，所以通常使用cls命名做区分(非强制)
	在类内可以直接使用类方法或类变量，无法直接使用实例变量或方法
	调用：
	无需实例化，直接通过 类.方法名 调用，也可以通过 实例.方法名 调用
	# 1. 类的定义
	class MethodsDemo:
		param_a = 0
		# 定义类方法必须加 classmethod装饰器
		@classmethod
		def classmethod_demo(cls):
			"""
			类方法，第一个参数需要改为cls
			:return:
			"""
			print("类方法", cls.param_a)

	# 2. 类的调用
	MethodsDemo.classmethod_demo() # 无需实例化，直接调用
04、静态方法
	定义：
	使用 @staticmethod 装饰器，没有和类本身有关的参数
	无法直接使用任何类变量、类方法或者实例方法、实例变量
	调用：
	无需实例化，直接通过 类.方法名 调用，也可以通过 实例.方法名 调用
	# 1. 定义
	class MethodsDemo:
		param_a = 0
		@staticmethod
		def static_demo():
			"""
			静态方法
			:return:
			"""
			print("静态方法") # 无法直接调用类变量
	# 2. 调用
	MethodsDemo.static_demo()
05、普通方法、类方法、静态方法
	名称	    定义	                 调用 	                            关键字	        使用场景
	普通方法	至少需要一个参数self	 实例名.方法名()	                无	            方法内部涉及到实例对象属性的操作
	类方法	    至少需要一个cls参数	     类名.方法名() 或者实例名.方法名()	@classmethod	如果需要对类属性，即静态变量进行限制性操作
	静态方法	无默认参数	             类名.方法名() 或者实例名.方法名()	@staticmethod	无需类或实例参与	
06、实际案例
	右边的代码实现的需求是格式化输出时间
	如果现在需求变更，输入 年、月、日 没法保证格式统一，可能是json，可能是其他格式的字符串，在不修改构造函数的前提下，如何更改代码
	class DateFormat:
		def __init__(self, year=0, month=0, day=0):
			self.year = year
			self.month = month
			self.day = day

		def out_date(self):
			return f"输入的时间为{self.year}年，{self.month}月，{self.day}日"
		
	year, month, day = 2017, 7, 1

	demo = DateFormat(year, month, day)
	print(demo.out_date())  
07、静态方法实际案例
	此方法没有任何和实例、类相关的部分，可以作为一个独立函数使用
	某些场景下，从业务逻辑来说又属于类的一部分
	例子：简单工厂方法
	# static 使用场景
	class HeroFactory:
		# staticmethod 使用场景，
		# 方法所有涉及到的逻辑都没有使用实例方法或者实例变量的时候
		# 伪代码
		@staticmethod
		def create_hero(hero):
			if hero == "ez":
				return EZ()
			elif hero == "jinx":
				return Jinx()
			elif hero == "timo":
				return Timo()
			else:
				raise Exception("此英雄不在英雄工厂当中")