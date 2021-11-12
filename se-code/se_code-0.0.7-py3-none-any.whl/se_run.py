# -*- coding: utf-8 -*-
# @Time    : 2021/11/11 14:25
# @Author  : wyw
import os
import sys
import se_import
from pathlib import PurePath
import pickle
class SE_Importer:
    def __init__(self,project_dir):
        project_dir = os.path.abspath(project_dir)
        self.project_dir = project_dir
        self.filename_data_info = os.path.join(self.project_dir, '__metadata__.pys')

        with open(os.path.join(self.project_dir, '__meta__.pys'),mode='rb') as f:
            se_single,rules,filemeta_map = pickle.load(f)

        for idx in range(len(rules)):
            rules[idx] = rules[idx].replace('/', '.')
            rules[idx] = rules[idx].replace('\\', '.')
        self.se_module_rules = rules
        self.filemeta_map = filemeta_map
        self.se_single = se_single
        self.mapper = {}

    def find_module(self, fullpath, path=None):
        p = PurePath(fullpath)
        flag = False
        for item in self.se_module_rules:
            if p.match(item):
                flag = True
                break
        if flag:
            if fullpath not in self.mapper:
                p = path._path if path is not None and hasattr(path, '_path') else path
                self.mapper[fullpath] = p[0] if p else None
        return self if flag else None
    def load_module(self, fullpath):
        base_item = fullpath.rpartition('.')[0]
        l_item = fullpath.rpartition('.')[-1]
        path = self.mapper[fullpath]
        if fullpath in sys.modules:
            return sys.modules[fullpath]
        if base_item in sys.modules:
            if l_item in sys.modules[base_item].__dict__:
                return sys.modules[base_item].__dict__[l_item]
        if not self.se_single:
            is_init_file = False
            filename = os.path.join(path,l_item + '.pys')
            if not os.path.exists(filename):
                is_init_file = True
                filename = os.path.join(path,  '__init__.pys')
            file_data = filename
            module_src = filename[:-1]
        else:
            is_init_file = False
            filename = fullpath.replace('.','/') + '.py'
            if filename not in self.filemeta_map:
                is_init_file = True
                filename = base_item.replace('.','/') + '/__init__.py'
            info = self.filemeta_map[filename]
            file_size = info['size']
            file_pos = info['pos']
            with open(self.filename_data_info,mode='rb') as f:
                f.seek(file_pos,0)
                file_data = f.read(file_size)
            filename = os.path.join(self.project_dir,filename)
            module_src = filename

        module_name = base_item if is_init_file else fullpath
        module = se_import.load_module_from_desfile(module_name,file_data,module_src)
        if module and l_item in module.__dict__:
            sub_module = module.__dict__[l_item]
            sys.modules[base_item] = module
            sys.modules[fullpath] = sub_module
            return sub_module
        sys.modules[module_name] = module
        return module


def se_ready(project_dir):
    sys.meta_path.insert(0, SE_Importer(project_dir))