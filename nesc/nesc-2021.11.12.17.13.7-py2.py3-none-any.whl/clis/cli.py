#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : MeUtils.
# @File         : __init__.py
# @Time         : 2021/1/31 10:20 下午
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : python meutils/clis/__init__.py
# /usr/bin/python3 cli.py


import typer

from meutils.pipe import *
from meutils.log_utils import logger4wecom
from meutils.decorators.catch import wecom_catch, wecom_hook

cli = typer.Typer(name="东北证券 clis")


@cli.command(help="help")  # help会覆盖docstring
@wecom_hook("东北证券cli测试")
@args
def clitest(path: str):
    """

    @param name: name
    @return:
    """

    p = Path(path)
    typer.echo(f"{p}")
    typer.echo(f"{p.absolute()}")


@cli.command()
@args
def extract4ddl(ipath: str, opath=None, encoding='GB18030', start_str='create table', end_str=')'):
    """解析ddl
    nesc extract4ddl '/Users/yuanjie/Desktop/notebook/0_TODO/mot_part.sql'
    """
    from nesc.extract import extract4ddl
    extract4ddl.main(ipath, opath, encoding=encoding, start_str=start_str, end_str=end_str)


@cli.command()
@args
def extract4excel(ipath: str, opath=None):
    """解析excel
    nesc extract4excel xx
    """
    from nesc.extract import extract4excel
    extract4excel.main(ipath, opath)


@cli.command()
@args
def text_match(target, file, topn: int = 10, batch_size: int = 256,
               model_home='chinese_roformer-sim-char-ft_L-6_H-384_A-6'):
    """相似文本匹配"""
    from nesc.sim import sim
    sim.main(target, file, topn, batch_size, model_home)


@cli.command()
@args
def text_match_v2(target, file, topn: int = 10, batch_size: int = 256,
                  model_home='chinese_roformer-sim-char-ft_L-6_H-384_A-6'):
    """相似文本匹配
    nesc text-match-v2 '手机号' '标准字段.txt'
    """
    from nesc.sim import simv2
    simv2.main(target, file, topn, batch_size, model_home)


def _run_cmd(cmd, nohup=0):
    cmd = f"nohup {cmd} &" if nohup else cmd
    logger.debug(cmd)
    return os.system(cmd)


@cli.command()
@args
def run(app_file: str, app='fastapi', port=9993, nohup=0):
    """Support fastapi/streamlit/gradio/gui app."""
    if not Path(app_file).exists():
        app_file = Path(get_module_path(f'../apps_{app}', __file__)) / app_file

    if app in ('fastapi', 'gui', 'gradio'):
        cmd = f"python {app_file}"
    elif app == 'streamlit':
        cmd = f"streamlit run {app_file} --server.baseUrlPath web --server.port {port}"
    else:
        cmd = "echo 无app可用"

    _run_cmd(cmd, nohup)


if __name__ == '__main__':
    cli()
