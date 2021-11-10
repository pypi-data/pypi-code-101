# -*- coding: utf-8 -*-

import os; os.chdir("S:/siat")
from siat.fama_french import *

ff3=get_ff_factors('2016-1-1','2020-12-31','Europe','FF3','yearly')
mom=get_ff_factors('2016-1-1','2020-12-31','Europe','Mom','yearly')

get_ffc4_factors('2016-1-1','2020-1-1','Europe','yearly')

get_ffc4_factors('2021-10-20','2021-10-30','US','daily')


ff3_betas=reg_ff3_betas('AAPL','2018-1-1','2019-4-30','US')
ff3_betas=reg_ff3_betas('BILI','2018-1-1','2019-4-30','US')

ff3_betas=reg_ff3_betas('BMW.DE','2018-1-1','2019-4-30','Europe')
ff3_betas=reg_ff3_betas('AEM','2018-3-1','2019-8-31','US')

reg_ffc4_betas('JD','2018-1-1','2019-4-30','US')
reg_ffc4_betas('BABA','2018-1-1','2019-4-30','US')
reg_ffc4_betas('MSFT','2018-1-1','2019-4-30','US')
reg_ffc4_betas('TAL','2018-1-1','2019-4-30','US')

get_ff5_factors('2019-5-20','2019-5-31','US','daily')
get_ff5_factors('2018-1-1','2019-4-30','US','monthly')

reg_ff5_betas('PTR','2018-1-1','2019-4-30','US')
reg_ff5_betas('QCOM','2018-1-1','2019-4-30','US')


    try:
        factor_df=ds[seq]
    except:
        extract_DESCR(ds)
        
        
def extract_DESCR(ds):
    """
    归纳：从字典的DESCR中提取年度因子信息 ，用于seq缺失1但误放置在DESCR中的情形
    """        
    descr_str=factor_df=ds['DESCR']
    wml_pos=descr_str.find("WML")
    nn_pos=descr_str.find("\n\n ")
    wml_post=descr_str[wml_pos+4:nn_pos]
    wml_post1=wml_post.replace('  ,',',')
    wml_post2=wml_post1.replace(' ,',',')
    wml_post3=wml_post2+' '
    
    #正则表达式提取配对
    import re
    wml_post_list=re.findall(r"(.+?),(.+?) ", wml_post3)    
    
    import pandas as pd
    df = pd.DataFrame(columns=('Date', 'Mom'))
    for i in wml_post_list:
        #print(i[0],i[1])
        s = pd.Series({'Date':i[0], 'Mom':float(i[1])})
        # 这里 Series 必须是 dict-like 类型
        df = df.append(s, ignore_index=True)
        # 这里必须选择ignore_index=True 或者给 Series一个index值    
    df.set_index('Date',drop=True, inplace=True)
    
    return df
    
    
    
    
    