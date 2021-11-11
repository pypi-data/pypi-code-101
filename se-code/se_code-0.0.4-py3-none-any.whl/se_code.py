# @Time    : 2021/11/10 20:23
# @Author  : tk
# @FileName: py_code.py

import os
import shutil
import se_import
from pathlib import PurePath
def se_project(src_dir,
                dst_dir,
                ignore = shutil.ignore_patterns('test','.git','.idea','setup.py'),
                rules = ['serving/utils/*','serving/run*','serving/http_client/http*'],
                key=bytes([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),
                iv=bytes([1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
):

    shutil.copytree(src_dir,dst_dir,ignore=ignore)
    for root,dirs,filename_list in os.walk(dst_dir):
        for filename in filename_list:
            if not filename.endswith('.py'):
                continue

            file_src = os.path.join(root, filename)
            file_dst = os.path.join(root, filename + 's')

            p = PurePath(file_src)
            flag = False
            for item in rules:
                if p.match(item):
                    flag = True
                    break
            if not flag:
                continue
            b = se_import.dump_module_to_desfile(file_src,key,iv)
            with open(file_dst,mode='wb') as f:
                f.write(b)
            os.remove(file_src)