# -*- coding: utf-8 -*-
# @Time    : 2021/11/11 14:25
# @Author  : wyw
import os
import sys
import se_import
from pathlib import PurePath
class SE_Importer:
    def __init__(self,rules = ['serving/utils/*','serving/run*','serving/http_client/http*']):
        self.mapper = {}
        for idx in range(len(rules)):
            rules[idx] = rules[idx].replace('/', '.')
            rules[idx] = rules[idx].replace('\\', '.')
        self.se_module_rules = rules
    def find_module(self, fullpath, path=None):
        p = PurePath(fullpath)
        flag = False
        for item in self.se_module_rules:
            if p.match(item):
                flag = True
                break
        if flag:
            if fullpath not in self.mapper:
                self.mapper[fullpath] = path[0] if path else None
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

        filename = os.path.join(path,l_item + '.pys')
        if not os.path.exists(filename):
            filename = os.path.join(path,  '__init__.pys')
            module_name = base_item
            module_src = path + '/__init__.py'
        else:
            module_name = fullpath
            module_src = path + '/' + l_item + '.py'

        module = se_import.load_module_from_desfile(module_name,filename,module_src)
        if module and l_item in module.__dict__:
            sub_module = module.__dict__[l_item]
            sys.modules[base_item] = module
            sys.modules[fullpath] = sub_module
            return sub_module
        sys.modules[module_name] = module
        return module


def se_ready(rules):
    sys.meta_path.insert(0, SE_Importer(rules))