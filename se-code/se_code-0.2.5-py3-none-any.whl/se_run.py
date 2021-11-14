# -*- coding: utf-8 -*-
# @Time    : 2021/11/11 14:25
# @Author  : wyw
import os
import sys
import se_import
from pathlib import PurePath
import pickle

'''
   注册运行解析器
        register_module(root_dir)
        root_dir 加密工程所在目录，如下所示 /home/project_se
        1.
        /home/project_se
                    script
                          run.sh #启动脚本
                          ...
                    serving # 源码模块所在目录
                                ...
                          utils
                                ...
                          runner.pys
'''

from collections import namedtuple

PackageMapper = namedtuple('_PackageMapper', ['module_key', 'name', 'src','is_init_file','is_sub_object'])

class SE_Importer:
    def __init__(self,root_dir):
        root_dir = os.path.abspath(root_dir)
        self.root_dir = root_dir
        with open(os.path.join(self.root_dir, '.__meta__.pys'),mode='rb') as f:
            package_name,ext,se_single,rules,filemeta_map = pickle.load(f)
        for idx in range(len(rules)):
            rules[idx] = rules[idx].replace('/', '.')
            rules[idx] = rules[idx].replace('\\', '.')
        self.package_name = package_name
        self.ext = ext
        self.se_module_rules = rules
        self.filemeta_map = filemeta_map
        self.se_single = se_single
        self.mapper = {}

    def get_file_info(self,fullpath, path):
        filename = None

        path_item = fullpath.rpartition('.')
        base_item = path_item[0]
        l_item = path_item[-1]

        p1 = PackageMapper(fullpath,  fullpath,os.path.join(path, l_item + self.ext),False,False)
        p2 = PackageMapper(base_item, base_item, os.path.join(path, '__init__' + self.ext), True, True)
        p3 = PackageMapper(base_item + '.__init__', base_item, os.path.join(path, '__init__' + self.ext) ,True, True)
        p4 = PackageMapper(fullpath + '.__init__', fullpath , os.path.join(path, l_item + '/__init__' + self.ext), True, False)
        arr = [p1, p2, p3, p4]
        module_name = None
        is_sub_object = False
        for item in arr:
            if item.module_key in self.filemeta_map:
                filename = item.src
                module_name = item.name
                is_init_file = item.is_init_file
                is_sub_object = item.is_sub_object
                filemeta = self.filemeta_map[item.module_key]
                break
        if filename is None:
            return None
        return  {
            'name' : module_name,
            'file': filename if not self.se_single else os.path.join(self.root_dir, '.__data__' + self.ext),
            'src': filename[:-len(self.ext)] + '.py',
            'pos': 0 if not self.se_single else filemeta['pos'],
            'size': filemeta['size'],
            'is_init_file' : is_init_file,
            'is_sub_object': is_sub_object,
        }
    def find_from_cache(self,fullpath,path):
        if fullpath not in self.mapper:
            p = path._path if path is not None and hasattr(path, '_path') else path
            real_path = p[0] if p and len(p) else self.root_dir
            file_info = self.get_file_info(fullpath, real_path)
            if file_info is None:
                return None
            self.mapper[fullpath] = file_info
        else:
            file_info = self.mapper[fullpath]
        return file_info

    def find_module(self, fullpath  , path=None):
        if self.package_name is not None and not fullpath.startswith(self.package_name):
            return None
        p = PurePath(fullpath)
        p2 = PurePath(fullpath + '.__init__')
        p3 = PurePath(fullpath.rpartition('.')[0] + '.__init__') if fullpath.rfind('.') > 0 else None
        flag = False
        for item in self.se_module_rules:
            if p.match(item) or p2.match(item) or (p3 and p3.match(item)) :
                flag = True
                break
        if not flag:
            return None
        file_info = self.find_from_cache(fullpath,path)
        return self if file_info is not None else None


    def load_module(self, fullpath):
        base_item = fullpath.rpartition('.')[0]
        l_item = fullpath.rpartition('.')[-1]

        if fullpath in sys.modules:
            return sys.modules[fullpath]
        if base_item in sys.modules:
            if l_item in sys.modules[base_item].__dict__:
                return sys.modules[base_item].__dict__[l_item]

        filemeta = self.mapper[fullpath]
        name = filemeta['name']
        file = filemeta['file']
        src = filemeta['src']
        file_size = filemeta['size']
        file_pos = filemeta['pos']
        is_init_file = filemeta['is_init_file']
        is_sub_object = filemeta['is_sub_object']

        if file_size > 0:
            with open(file,mode='rb') as f:
                f.seek(file_pos,0)
                file_data = f.read(file_size)
        else:
            file_data = bytes("",encoding='utf-8')
        module = se_import.load_module_from_desfile(name,file_data,src)
        if is_init_file and is_sub_object and module and l_item in module.__dict__:
            sub_module = module.__dict__[l_item]
            sys.modules[base_item] = module
            sys.modules[fullpath] = sub_module
            return sub_module
        sys.modules[name] = module
        return module
'''
root_dir 所在目录
'''
def se_register_module(root_dir : str):
    sys.meta_path.append(SE_Importer(root_dir))