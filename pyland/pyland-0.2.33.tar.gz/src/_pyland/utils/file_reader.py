# -*- coding: utf-8 -*-
"""
文件读取。YamlReader读取yaml文件，ExcelReader读取excel。
"""
from yaml import safe_load_all as y_safe_local_all
from json import load as j_load
from os import path
from xlrd import open_workbook


class YamlReader(object):
    def __init__(self, file_path):
        if path.exists(file_path):
            self.file_path = file_path
        else:
            raise FileNotFoundError('文件{}不存在！'.format(file_path))
        self._data = None

    @property
    def data(self):
        # 如果第一次调用data，读取yaml文档，否则直接返回之前保存的数据
        if not self._data:
            with open(self.file_path, 'rb') as f:
                self._data = list(y_safe_local_all(f))  # load后是个generator，用list组织成列表
        return self._data


class JsonReader(YamlReader):
    @property
    def data(self):
        if not self._data:
            with open(self.file_path, 'rb') as f:
                self._data = j_load(f)
        return self._data


class RawReader(YamlReader):
    @property
    def data(self):
        if not self._data:
            with open(self.file_path, 'r', encoding="utf8") as f:
                self._data = f.read()
        return self._data


class SheetTypeError(Exception):
    pass


class ExcelReader():
    """
    读取excel文件中的内容。返回list。

    如：
    excel中内容为：
    | A  | B  | C  |
    | A1 | B1 | C1 |
    | A2 | B2 | C2 |

    如果 print(ExcelReader(excel, title_line=True).data)，输出结果：
    [{A: A1, B: B1, C:C1}, {A:A2, B:B2, C:C2}]

    如果 print(ExcelReader(excel, title_line=False).data)，输出结果：
    [[A,B,C], [A1,B1,C1], [A2,B2,C2]]

    可以指定sheet，通过index或者name：
    ExcelReader(excel, sheet=2)
    ExcelReader(excel, sheet='BaiDuTest')
    """
    def __init__(self, excel, sheet=0, title_line=True):
        if path.exists(excel):
            self.excel = excel
        else:
            raise FileNotFoundError('文件不存在！ ')
        self.sheet = sheet
        self.title_line = title_line
        self._data = list()

    @property
    def data(self):
        if not self._data:
            workbook = open_workbook(self.excel)
            if type(self.sheet) not in [int, str]:
                raise SheetTypeError('Please pass in <type int> or <type str>, not {0}'.format(type(self.sheet)))
            elif type(self.sheet) == int:
                s = workbook.sheet_by_index(self.sheet)
            else:
                s = workbook.sheet_by_name(self.sheet)

            if self.title_line:
                title = s.row_values(0)  # 首行为title
                for col in range(1, s.nrows):
                    # 依次遍历其余行，与首行组成dict，拼到self._data中
                    self._data.append(dict(zip(title, s.row_values(col))))
            else:
                for col in range(0, s.nrows):
                    # 遍历所有行，拼到self._data中
                    self._data.append(s.row_values(col))
        return self._data


if __name__ == '__main__':
    yml = '../config/config.yml'
    reader = YamlReader(yml)
    print(reader.data[1])

    xls = '../data/vid_feature_int384_sensenets_V6_20181211.xlsx'
    reader = ExcelReader(xls, title_line=False)
    print(reader.data[0][1])







