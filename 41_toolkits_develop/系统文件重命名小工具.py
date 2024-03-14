#系统文件批量重命名小工具
import os
from colorama import init, Fore, Style

init()
print(Fore.LIGHTBLACK_EX + "\n\t\t\t\t<<<<< 欢迎使用批量重命名文件小工具 >>>>>\n" + Style.RESET_ALL)

while True:
  try:
    folder_path = input(Fore.YELLOW + "请输入需要批量重命名文件的目录位置：\n" + Style.RESET_ALL)
    index = 0
    if len(os.listdir(folder_path)) == 0:

      print(Fore.BLUE + "该目录下文件为空，已重新为你启动程序\n" + Style.RESET_ALL)
      continue
    prefix_name = input(Fore.YELLOW + "请输入重命名后的文件前缀（如果不需要前缀，请直接回车）：\n" + Style.RESET_ALL)
    print("\t旧文件名：>>>\t新文件名")
    for filename in os.listdir(folder_path):
      index += 1
      file_path = os.path.join(folder_path, filename)
      if os.path.isfile(file_path):
          name, ext = os.path.splitext(filename)
          new_name = prefix_name + str(index) + ext
          print("\t"+name + "：>>>\t" +new_name)
          os.rename(file_path, os.path.join(folder_path, new_name))
    isExit = input(Fore.LIGHTGREEN_EX + "\nSUCCESS： 文件重命名完成，输入字母 y 继续运行，输入其他或回车直接退出：\n" + Style.RESET_ALL)
    if isExit != 'y':
       break
  except:
    isExit = input(Fore.RED + "\nERROR： 你的文件目录不正确，请检查。输入字母 y 继续运行，输入其他或回车直接退出：\n" + Style.RESET_ALL)
    if isExit != 'y':
       break
    pass
