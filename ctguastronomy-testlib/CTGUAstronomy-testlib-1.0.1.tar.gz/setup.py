from setuptools import setup

def readme_file():
    with open("README.rst") as wb:
        return wb.read()

setup(
    name='CTGUAstronomy-testlib',           # 名称
    version='1.0.1',                        # 版本
    description='A normal test file',       # 描述信息
    packages=['package'],                   # 多文件模块
    py_modules=['read_fits'],               # 单文件模块
    author='ctguer_liuchvn',                # 作者
    author_email='liuchvn@qq.com',          # 作者邮箱
    long_description='readme_file()'        # 长描述
    # install_requires='',                  # 其他依赖的包
)
