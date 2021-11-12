# @Time    : 2021/11/10 20:23
# @Author  : tk
# @FileName: py_code.py

import os
import shutil
import se_import
from pathlib import PurePath
import pickle

def se_project(src_dir,
    dst_dir,
    dst_exists_remove=False,
    se_single = False,
    ignore = shutil.ignore_patterns('test','.git','.idea','setup.py'),
    rules = ['serving/utils/*','serving/run*','serving/http_client/http*'],
    key=bytes([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),
    iv=bytes([1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
):
    src_dir = os.path.abspath(src_dir)
    dst_dir = os.path.abspath(dst_dir)

    if dst_exists_remove and os.path.exists(dst_dir):
        shutil.rmtree(dst_dir)
    shutil.copytree(src_dir,dst_dir,ignore=ignore)

    file_list = []
    filemeta_map = {}
    fp_pos = 0
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
            file_list.append((file_src,file_dst,b))

            file_src = os.path.abspath(file_src)
            file_src = file_src[len(dst_dir)+1:]
            file_src = file_src.replace('\\','/')

            filemeta_map[file_src] = {
                'file': file_src,
                'size': len(b),
                'pos': fp_pos
            }
            fp_pos += len(b)

    filename_meta = os.path.join(dst_dir,'__meta__.pys')
    with open(filename_meta,mode='wb') as f:
        pickle.dump((se_single,rules,filemeta_map),f)
    if not se_single:
        for item in file_list:
            file_src = item[0]
            file_dst = item[1]
            b = item[2]
            with open(file_dst, mode='wb') as f:
                f.write(b)
            os.remove(file_src)
    else:
        filename_data_info = os.path.join(dst_dir,'__metadata__.pys')
        with open(filename_data_info,mode='wb') as f:
            for item in file_list:
                file_src = item[0]
                b = item[2]
                f.write(b)
                os.remove(file_src)
