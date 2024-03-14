#coding:utf-8

import sys
import time
for i in range(10):
    if i == 6:
        print("exit...")
        sys.exit()
    print(f'running{i}...')
    print(sys.getdefaultencoding())  # 获取系统当前编码
    time.sleep(1)

print(sys.getdefaultencoding())  # 获取系统当前编码