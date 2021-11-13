# -*- coding: utf-8 -*-
import json
import os
import sys
from platform import python_version_tuple
import re

from idebug import *
from ipylib.ipath import clean_path


__all__ = [
    'Configuration',
]


class DBHandler:

    def __init__(self, dic):
        for k,v in dic.items():
            # db 관련 값의 데이타-타입을 청소한다
            if isinstance(v, str):
                if v.isnumeric():
                    v = int(v)
                elif v in ['True','False']:
                    v = bool(v)
                elif v == 'None':
                    v = None
            setattr(self, k, v)

    @property
    def name(self): return self.DBName

class PathHandler:

    def __init__(self, dic):
        for k,v in dic.items():
            setattr(self, k, v)
        # 운영체제 타입에 따라 "프로젝트들이 모여있는 폴더 경로"를 잡아준다

    def _adjust_path(self, p):
        if os.name != 'nt':
            if self.base['Windows'] in p:
                p = p.replace(self.base['MacOS'])
        return clean_path(p)

    @property
    def BasePath(self):
        p = self.base['Windows'] if os.name == 'nt' else self.base['MacOS']
        return clean_path(p)
    @property
    def ProjectPath(self): return self._adjust_path(self.project)
    @property
    def BackupPath(self): return clean_path(self.backup)
    @property
    def SchemaCSVPath(self): return self._adjust_path(self.data['schema'])
    @property
    def StaticSchemaCSVPath(self): return self._adjust_path(self.data['schema']['static'])
    @property
    def DynamicSchemaCSVPath(self): return self._adjust_path(self.data['schema']['dynamic'])
    @property
    def ManDataJSONPath(self): return self._adjust_path(self.data['mandata'])
    @property
    def DevGuideTextPath(self): return self._adjust_path(self.data['devguide'])

class JSONHandler:

    def __init__(self):
        pass

    @property
    def ConfigDir(self): return os.path.dirname(__file__)
    @property
    def DefaultFilePath(self): return f'{self.ConfigDir}/default.json'
    @property
    def DefaultConfig(self):
        # 기본 설정값(default.json) 읽어들인다
        f = open(self.DefaultFilePath, mode='r')
        text = f.read()
        f.close()
        return json.loads(text.strip())

    def save(self):
        # 사용자가 변경한 설정값을 별도로 저장한다
        js = json.dumps(self.__dict__)
        print('json_str:', js)
        self._write_user_setting(js)

    def _write_user_setting(self, json_str):
        path = self.ConfigDir
        f = open(f'{path}/user.json', mode='w')
        f.write(json_str)
        f.close()

class Configuration:

    def __init__(self):
        self.fhandler = JSONHandler()
        for k,v in self.DefaultConfig.items():
            if k == 'path': v = PathHandler(v)
            elif k == 'db': v = DBHandler(v)
            setattr(self, k, v)

    @property
    def DefaultConfig(self): return self.fhandler.DefaultConfig
    @property
    def ProjectName(self): return self.general['ProjectName']

    @funcIdentity
    def view(self):
        for k,v in self.__dict__.items():
            SectionGubun(k)

            if isinstance(v, dict): pp.pprint(v)
            else: dbg.dict(v)
