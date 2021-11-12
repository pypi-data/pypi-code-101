# -*- coding: utf-8 -*-
# @Time    : 2021/11/11 14:42
# @Author  : wyw
import shutil

'''
    2021-11-12 新增功能:
    se_single 对整个工程代码加密成单独文件, 可避免目录结构暴露 
'''

#工程源码加密处理

#src_dir 工程源码   dst_dir加密处理工程，需保证文件夹不存在
def test_se_project(src_dir = '/home/project',dst_dir = '/home/project_se'):
    from se_code import se_project
    #源码工程目录示例,
    # 代码 /home/project/serving ,
    # 代码 /home/project/serving/utils ,等等
    # 代码 /home/project/serving/runner.py 程序主入口 main()
    # script运行脚本 /home/project/script
    # /home/project/script/run.sh 启动脚本

    #文件夹存在则自动删除
    dst_exists_remove = False

    #对工程代码加密成单独文件
    se_single = False

    #忽略复制文件，文件对工程运行没有用
    ignore = shutil.ignore_patterns('test','.git','.idea','setup.py')

    #加密接受规则
    rules = ['serving/utils/*', 'serving/run*', 'serving/http_client/http*']
    se_project(src_dir,
        dst_dir,
        dst_exists_remove=dst_exists_remove,
        se_single=se_single,
        ignore = ignore,
        rules = rules,
        key=bytes([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),
        iv=bytes([1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    )

def run():
    #将下面代码放到对应加密后的代码工程用于启动， 例如 /home/project_se/serving/start.py
    import sys
    sys.path.append('..')
    from se_code import se_ready
    project_dir = '/home/project_se'
    se_ready(project_dir=project_dir)
    from serving.runner import main
    main()
