import os
import tkinter as tk
from tkinter import filedialog


# 文件批量顺序、连续重命名工具
class FileRenamerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("文件批量顺序连续重命名工具")

        self.path_var = tk.StringVar()
        self.string_var = tk.StringVar()
        self.i_var = tk.IntVar()
        self.suff_var = tk.StringVar()  # 新增变量用于存储文件后缀

        self.create_widgets()

    def create_widgets(self):
        # 用于显示所选路径的标签
        path_label = tk.Label(self.master, text="所选路径:")
        path_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        # 用于显示所选路径的输入框
        path_entry = tk.Entry(self.master, textvariable=self.path_var, state="readonly", width=50)
        path_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        # 用于选择路径的按钮
        browse_button = tk.Button(self.master, text="浏览", command=self.select_path)
        browse_button.grid(row=0, column=2, padx=10, pady=10, sticky=tk.W)

        # 输入字符串的标签和输入框
        string_label = tk.Label(self.master, text="字符串(可为空):")
        string_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        string_entry = tk.Entry(self.master, textvariable=self.string_var, width=20)
        string_entry.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

        # 输入起始索引的标签和输入框
        i_label = tk.Label(self.master, text="起始字符串（数字）:")
        i_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
        i_entry = tk.Entry(self.master, textvariable=self.i_var, width=10)
        i_entry.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

        # 输入文件后缀的标签和输入框
        suff_label = tk.Label(self.master, text="文件后缀(例.jpg):")
        suff_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
        suff_entry = tk.Entry(self.master, textvariable=self.suff_var, width=10)
        suff_entry.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W)

        # 执行重命名的按钮
        rename_button = tk.Button(self.master, text="重命名", command=self.rename_files)
        rename_button.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

        # 监听string_var的变化
        self.string_var.trace_add("write", self.check_string)

        # 用于显示输出结果的Text组件
        self.result_text = tk.Text(self.master, height=3, width=60, state="disabled")
        self.result_text.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

    def select_path(self):
        selected_path = filedialog.askdirectory()
        if selected_path:
            self.path_var.set(selected_path)

    def check_string(self, *args):
        # 检查字符串是否为空，如果为空，设置默认值
        if not self.string_var.get():
            self.string_var.set("")

    def rename_files(self):
        path = self.path_var.get()
        string = self.string_var.get()
        i = self.i_var.get()
        suff = self.suff_var.get()  # 获取文件后缀
        if path and suff:  # 确保路径和文件后缀非空
            filelist = os.listdir(path)
            filelist.sort()
            total_num = len(filelist)
            success_count = 0

            for item in filelist:
                if item.endswith(suff):
                    src = os.path.join(path, item)
                    dst = os.path.join(os.path.abspath(path), f"{string}{i}{suff}")
                    try:
                        os.rename(src, dst)
                        i += 1
                        success_count += 1
                    except Exception as e:
                        print(e)
                        print('重命名目录失败\r\n')

            result_message = f'共有 {total_num} 个文件需要重命名，成功转换 {success_count} 个文件'
            self.result_text.configure(state="normal")
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, result_message)
            self.result_text.configure(state="disabled")


if __name__ == "__main__":
    root = tk.Tk()
    app = FileRenamerApp(root)
    root.mainloop()