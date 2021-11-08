"""
[Important!!!  DO NOT TOUCH!!!]
"""
import os
from pyland import Config


pytest_plugins = 'pytester'


def pytest_addoption(parser):
    parser.addoption('--case-manage', required=False, help='analysis cases to manage by platform')


def pytest_generate_tests(metafunc):
    res = {}
    res['extra'] = {}
    res['extra']['params'] = {}

    for param in metafunc.fixturenames:
        if param.startswith('param'):
            if not param.endswith('valid'):
                param = param + '_valid'
            if hasattr(metafunc.module, 'combined'):
                param_pool = metafunc.module.combined[param]
                metafunc.parametrize(param, param_pool)
                # res['extra']['params'][param] = param_pool
            else:
                raise ValueError(f"param {param} set, but not found `combined`")
            
    project_path = metafunc.config.getoption('--case-manage')

    if project_path:
        for mark in metafunc.definition.iter_markers():
            if mark.name == 'allure_display_name':
                res['name'] = mark.args[0]
            elif mark.name == 'allure_label':
                label_type = mark.kwargs['label_type']
                label_value = mark.args[0]
                res['extra'][label_type] = label_value

        res['extra']['nodeID'] = metafunc.definition.nodeid
        res['extra']['path'] = metafunc.definition.location[0]
        res['extra']['module'] = metafunc.module.__name__
        if hasattr(metafunc.module, '__author__'):
            res['author'] = metafunc.module.__author__
        else:
            res['author'] = 'has no author yet'
        res['extra']['class'] = metafunc.cls.__name__ if metafunc.cls else None
        res['extra']['function'] = metafunc.function.__name__
        res['description'] = 'has no description yet' if not metafunc.function.__doc__ else metafunc.function.__doc__
        res['primary_key'] = 'extra.nodeID'
        res['category'] = 'pyland'
        res['priority'] = res['extra'].get('severity') if res['extra'].get('severity') else ''

        cfg = Config(path=project_path)
        case_manage_yml = os.path.join(cfg.DATA_PATH, '.tmp_case_manage.yml')
        cfg.update([res], case_manage_yml)

