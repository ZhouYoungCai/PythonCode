import pandas as pd
import numpy as np


class ExcelToPivot(object):
    def __init__(self, filename, file_path):
        self.file_name = filename
        self.file_path = file_path

    """
        excel自动转透视表功能
        返回透视结果
    """

    def excel_Pivot(self):
        print(self.file_path)
        data = pd.read_excel(self.file_path)
        data_pivot_table = pd.pivot_table(data, index=['供应商名称', '月份'], values=["入库金额"], aggfunc=np.sum)
        return data_pivot_table

    """
        按条件筛选，并保存
    """

    def select_data(self, name, month):
        data_pivot_table = self.excel_Pivot()
        data_new = data_pivot_table.query('供应商名称 == ["{}"] & 月份 == {}'.format(name, month))
        data_new.to_excel('{}.xlsx'.format(str(self.file_name).split('.')[0]))
        return '筛选完成！'


if __name__ == '__main__':
    filename = input("请输入文件名字：")
    path = 'C:/Users/80792/Desktop/' + filename
    pross = ExcelToPivot(filename, path)
    print(pross.select_data("C", 4))