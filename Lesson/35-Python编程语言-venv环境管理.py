01、venv 虚拟环境
	虚拟环境是什么
	虚拟环境的用途
	venv & virtualenv
02、venv 虚拟环境的优点
	独立的 Python 环境，不会产生冲突
	有助于包的管理
	删除和卸载方便
03、venv 使用方法
	创建虚拟环境
	激活虚拟环境
	安装 Python 包
04、venv 创建虚拟环境
	执行指令
	python3 -m venv test
05、venv 激活虚拟环境
	切换指定文件夹
	Windows：/Scripts/
	macOS：/bin/
	执行指令：activate
	# Windows 系统激活虚拟环境
	cd test
	cd Scripts
	activate

	# macOS系统激活虚拟环境
	cd test
	cd bin
	source actiavte
	# 或者一步到位
	source ./test/bin/acitvate
06、venv 安装 Python 包
	Python 版本选择
	进入 python2.7 环境：python2
	进入 python3.x 环境: python3
	pip 安装 Python 包
	安装 Python2.x 版本的包
	安装 Python3.x 版本的包
	# 进入 python2.7 环境
	python2

	# 进入 python3.x 环境
	python3

	# 安装 Python2.x 版本的包
	pip install xxx

	# 安装 Python3.x 版本的包
	pip3 install xxx
07、venv 退出和删除
	退出虚拟环境：deactivate
	删除虚拟环境：删除环境目录
	# Windows和macOS通用的退出指令
	deactivate