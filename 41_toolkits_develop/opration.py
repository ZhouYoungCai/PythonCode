from tkinter import Tk, Entry, Button, mainloop
import tkinter.filedialog
import excel_to_pivot
from tkinter import messagebox
from tkinter import ttk


def Upload():
    global filename, data_pivot_table
    try:
        filename = tkinter.filedialog.askopenfilename(title='选择文件')
        pross = excel_to_pivot.ExcelToPivot(str(filename).split('/')[-1], filename)
        data_pivot_table = pross.excel_Pivot()
        messagebox.showinfo('Info', '转换成功！')
    except Exception as e:
        print(e)
        messagebox.showinfo('Info', '转换失败！')


def select(name, month):
    try:
        print('供应商名称 == ["{}"] & 月份 == {}'.format(name, month))
        data_new = data_pivot_table.query('供应商名称 == ["{}"] & 月份 == {}'.format(name, month))
        data_new.to_excel('{}.xlsx'.format(str(filename).split('.')[0]))
        messagebox.showinfo('Info', '筛选完成并生成文件！')
        root.destroy()
    except Exception as e:
        print(e)
        messagebox.showinfo('Info', '筛选失败！')


root = Tk()
root.config(background="#6fb765")
root.title('自动转透视表小工具')
root.geometry('500x250')
e1 = Entry(root, width=30)
e1.grid(row=2, column=0)

btn1 = Button(root, text=' 上传文件 ', command=Upload).grid(row=2, column=10, pady=5)

box1 = ttk.Combobox(root)
# 使用 grid() 来控制控件的位置
box1.grid(row=5, sticky="NW")
# 设置下拉菜单中的值
box1['value'] = ('A', 'B', 'C', 'D', '供应商')
# 通过 current() 设置下拉菜单选项的默认值
box1.current(4)

box2 = ttk.Combobox(root)
box2.grid(row=5, column=1, sticky="NW")
box2['value'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, '月份')
box2.current(12)


# 编写回调函数，绑定执行事件
def func(event):
    global b1, b2
    b1 = box1.get()
    b2 = box2.get()


# 绑定下拉菜单事件
box1.bind("<<ComboboxSelected>>", func)
box2.bind("<<ComboboxSelected>>", func)
btn2 = Button(root, text=' 筛选数据 ', command=lambda: select(b1, b2)).grid(row=30, column=10, pady=5)
mainloop()