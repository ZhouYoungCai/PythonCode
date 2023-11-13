01、pip概述
    pip是python包管理工具
	    python2的2.7.9版本开始自带
		python3的3.4版本开始自带
	https://pypi.org/  托管了大量流行的python
02、pip常用命令
    功能         指令
	查看pip版本  pip -V
	查看帮助文档 pip help
	查看包列表   pip list
	导出包列表   pip freeze
	安装包       pip install 包名
	升级         pip install -U 包名
	卸载         pip uninstall 包名
03、pip 安装包
	普通安装
	指定版本
	从文件中安装
	# 默认安装最新版本
	$ pip install pytest

	# 执行版本
	$ pip install pytest==6.2.0

	# 从文件清单中批量安装
	$ pip install -r requirments.txt

	# 文件格式
	pytest==6.2.0
	Faker==9.3.1
	selenium==3.14.1
04、pip 升级包
	升级已安装的 Python 包
	$ pip install -U pytest
05、pip 卸载包
	卸载 Python 包
	# 卸载包

	$ pip uninstall pytest
06、pip 使用镜像加速
	pip install -i 镜像源

	国内常用源

	阿里源：https://mirrors.aliyun.com/pypi/simple/
	清华源：https://pypi.tuna.tsinghua.edu.cn/simple/
	豆瓣源：http://pypi.douban.com/simple/
	# 使用镜像

	pip install pytest -i https://pypi.douban.com/simple