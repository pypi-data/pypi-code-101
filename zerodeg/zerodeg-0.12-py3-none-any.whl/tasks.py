from MixacLib import cons
import time
import sys

usetime = time.time()

cons.inf('ZeroD-Core 任务列表程序')

cons.inf('setupBotWorkspace     创建机器人项目工作区')

usetime = time.time() - usetime

cons.inf(f'任务 完成，耗时{usetime}秒')
