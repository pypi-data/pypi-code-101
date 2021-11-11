from distutils.core import setup

setup(
    name='223', # 对外我们模块的名字
    version='1.0', # 版本号
    description='这是第一个对外发布的模块，测试哦', #描述
    author='zhangxin', # 作者
    author_email='11654743140@qq.com', py_modules=['223.game'] # 要发布的模块
)
