import pandas as pd
import numpy as np
import math
import sys
import os

class AmaSalesEstimator(object):
    """ 亚马逊预计销量计算器
    
    根据亚马逊大部分的一级类目BSR来计算产品当前的预计日销量或月销量。
    由于模型问题，对BSR为200以上的Listing估算效果较差，暂不开放BSR在该区间内的销量估算。

    Arrtibutes:
        df_temp_para: 最近一次导出参数的临时保存表，默认为None，用于缓存参数加速销量的计算。
        sales: 计算的预计日销量。
    
    Usage:
        AmaSalesEstimator(<paradata_path>, 'us', 'Home & Kitchen',95623).sales
            地区为us，一级类目为Home & Kitchen，BSR为95623的预计日销量
        AmaSalesEstimator(<paradata_path>, 'us', 'Home & Kitchen', 221563, True).sales
            地区为us，一级类目为Home & Kitchen，BSR为221563的预计月销量
    """
    df_temp_para = None
    sales = None

    def __init__(self, paradata_path, cy, cate, bsr, monthly = False):
        """ 寻找并提取对应的参数表，计算与BSR相应的预计日销量

        Args:
            paradata_path: 参数文件的地址，字符串格式。
            cy: 国家地区，字符串格式，用两位英文字母来表示。
            cate: 一级类目名称，字符串格式，必须严格按照亚马逊上显示的一级类目来填写。
            bsr: 一级类目的BSR值，整数格式。

        Raise:
            BSRError: 输入的BSR在200以内，无法正确预估日销量。
            ParaError: 当文件夹内没有参数表sales_est_para.xlsx时报错。
            CateError: 当所查询的类目没有在参数表内有记录时报错。
        """
        #验证输入的bsr值是否在200以内
        cy = cy.lower()
        cate = cate.strip()
        bsr = int(bsr)
        if bsr >= 200:
            pass
        else:
            sys.exit('BSRError: 输入的BSR在200以内，无法正确预估日销量')
        #导入计算用参数表
        if os.path.isfile(paradata_path):
            df_para = pd.read_excel(paradata_path)
        else:
            sys.exit('ParaError: 没有找到计算参数表sales_est_para.xlsx')
        #查看是否存在临时参数表
        if self.df_temp_para == None:
            df_temp_para = df_para[(df_para['cy'] == cy) & (df_para['cate'] == cate)]
            if df_temp_para['cy'].count() == 0:
                sys.exit('CateError: 没有在参数表内找到对应类目的参数，请检查类目名称或更新参数表')
            else:
                pass
            self.df_temp_para = df_temp_para
        else:
            #如果存在临时参数表，则查看是否和本次导入的一级类目一致
            if df_temp_para['cy'].iloc[0] == cy:
                pass
            else:
                df_temp_para = df_para[(df_para['cy'] == cy) & (df_para['cate'] == cate)]
                if df_temp_para['cy'].count() == 0:
                    sys.exit('CateError: 没有在参数表内找到对应类目的参数，请检查类目名称或更新参数表')
                else:
                    pass
                self.df_temp_para = df_temp_para
        list_para = df_temp_para[['a','b','c','d']].iloc[0].tolist()
        #计算公式
        def func(x,a,b,c,d):
            fx = a * x ** 3 + b * x ** 2 + c * x + d
            return fx
        #将输入的bsr转换为x
        x = np.log2(bsr)
        #计算
        fx = func(x, list_para[0], list_para[1], list_para[2], list_para[3])
        #如果计算结果小于1，则更改为0
        y = 2 ** fx
        if y < 1:
            y = 0
        else:
            pass
        #月销量开关
        if monthly == True:
            y = math.ceil(y * 30)
        else:
            y = math.ceil(y)
        self.sales = y