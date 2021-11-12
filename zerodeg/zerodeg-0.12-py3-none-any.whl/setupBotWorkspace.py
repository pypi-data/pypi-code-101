'''
零度 QQ机器人内核
工作区设置脚本
基于ZeroD-Core v0.12
你没看错，这就是仿照的Gradle
'''

from MixacLib import cons
import json
import os
import time
import sys

__cfg__ = json.dumps({
    'Name': 'Default',
    'Author': 'Default',
    'EventPort': '5701'
})
__PATH__ = os.getcwd()


time_start = time.time()


cons.inf(f'在{__PATH__}下运行任务[setupBotWorkspace]')


if not os.path.exists(__PATH__ + r'\zero.json'):
    cons.inf('创建zero.json')
    with open(__PATH__ + r'\zero.json', 'a') as cfg:
        cfg.write(__cfg__)
else:
    cons.error('错误：配置文件已存在，请确定此目录下没有已创建的工作区！')
    time_end = time.time()
    cons.error('构建失败，耗时{}秒'.format(time_end - time_start))
    sys.exit()


time_end = time.time()


cons.inf('构建完成，耗时{}秒'.format(time_end - time_start))
