from setuptools import setup,find_packages

with open("README.md", "r", encoding='utf8') as fh:
    long_description = fh.read()

setup(
    name = 'se-com-opts',
    version = '1.0.5',
    keywords = ('selenium'),
    description = '常用的selenium-webdriver设置',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license = 'MIT Licence',
    platforms = 'windows',

    author = 'JoeYoung',
    author_email = '1022104172@qq.com',
    url = 'https://gitee.com/joeyoung18/se_com_opts.git',

    py_modules = ['se_com_opts'],
    packages = find_packages(),
    include_package_data = True,
)