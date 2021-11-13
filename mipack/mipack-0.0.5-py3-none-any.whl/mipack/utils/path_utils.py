#!/usr/bin/env python
import os.path as osp


def module_path(module_name=''):
    rootdir = osp.dirname(osp.dirname(osp.abspath(__file__)))
    if module_name:
        return osp.join(rootdir, module_name)
    return rootdir
