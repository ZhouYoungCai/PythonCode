#coding:utf-8
import shutil
import os


def backup_file(source_file, dest_dir):
    # 检查源文件是否存在
    if not os.path.exists(source_file):
        print("源文件不存在！")
        return

    # 检查目标文件夹是否存在
    if not os.path.exists(dest_dir):
        print("目标文件夹不存在！")
        return

    # 备份文件
    shutil.copy(source_file, dest_dir)
    print("文件备份成功！")


# 示例用法
source_file = "path/to/source/file.txt"
dest_dir = "path/to/destination/directory"
backup_file(source_file, dest_dir)


