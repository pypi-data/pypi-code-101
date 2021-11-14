# @Time    : 2021/11/10 20:23
# @Author  : tk
# @FileName: py_code.py

import os
import shutil
import se_import
from pathlib import PurePath
import pickle
from pprint import pprint

'''
    src_dir 源工程路径
    dst_dir 加密工程路径
    package_name 如果制作.whl , 自定义设置包，否则默认为包含代码的最近目录名
    ext='.pys' 单独文件加密后缀
    dst_exists_remove 加密工程路径自动删除
    se_single = False 加密所有符合规则代码成一个文件
    ignore 复制忽略文件
    rules 加密规则，起始必须是根模块名
    key des key
    iv des iv
'''
def se_project(src_dir,
    dst_dir,
    package_name=None,
    ext='.pys',
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


    if package_name is None:
        for root, dirs, filename_list in os.walk(dst_dir):
            for filename in filename_list:
                if not filename.endswith('.py'):
                    f = os.path.join(root, filename)
                    f = f[len(dst_dir) + 1:]
                    f = f.replace('\\','/')
                    if f.find('/') == 0:
                        tmp_str = dst_dir.replace('\\', '/')
                        if tmp_str.find('/') != -1:
                            package_name = tmp_str.partition('/')[0]
                        break


    for root,dirs,filename_list in os.walk(dst_dir):
        for filename in filename_list:
            if not filename.endswith('.py'):
                continue
            file_src = os.path.join(root, filename)
            file_dst = os.path.join(root, filename[:-3] + ext)

            p = PurePath(file_src)
            flag = False
            for item in rules:
                if p.match(item):
                    flag = True
                    break
            if not flag:
                continue
            b = se_import.dump_module_to_desfile(file_src,key,iv)
            if not b:
                print('warning ' ,file_src, ' maybe an empty file')
            file_list.append((file_src,file_dst,b))

            my_file_src = os.path.abspath(file_src)
            my_file_src = my_file_src[len(dst_dir)+1:]

            my_file_src = my_file_src[0:-3]
            my_file_src = my_file_src.replace('\\','/')
            my_file_src = my_file_src.replace('/', '.')

            if package_name is not None:
                my_file_src = package_name + '.' + my_file_src
            filemeta_map[my_file_src] = {
                'file': my_file_src,
                'size': len(b) if b else 0,
                'pos': fp_pos
            }
            fp_pos += len(b) if b else 0

    if package_name is not None:
        package_name = package_name.replace('-','_')
        rules = [package_name + '/' + r for r in rules]

    filename_meta = os.path.join(dst_dir,'.__meta__.pys')
    with open(filename_meta,mode='wb') as f:
        pickle.dump((package_name,ext,se_single,rules,filemeta_map),f)


    pprint(filemeta_map.keys())

    if not se_single:
        for item in file_list:
            file_src = item[0]
            file_dst = item[1]
            b = item[2]
            with open(file_dst, mode='wb') as f:
                f.write(b)
            os.remove(file_src)
    else:
        filename_data_info = os.path.join(dst_dir,'.__data__' + ext)
        with open(filename_data_info,mode='wb') as f:
            for item in file_list:
                file_src = item[0]
                b = item[2]
                if b:
                    f.write(b)
                os.remove(file_src)
