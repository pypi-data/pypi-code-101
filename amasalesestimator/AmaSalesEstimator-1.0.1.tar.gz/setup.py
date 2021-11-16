from setuptools import setup,find_packages

with open("README.md", "r", encoding='utf8') as fh:
    long_description = fh.read()

setup(
    name = 'AmaSalesEstimator',
    version = '1.0.1',
    keywords = ('amazon','sales'),
    description = '亚马逊预计销量计算器',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license = 'MIT Licence',

    author = 'JoeYoung',
    author_email = '1022104172@qq.com',
    url = 'https://gitee.com/joeyoung18/AmaSalesEstiamtor',

    platforms = "any",
    py_modules = ['AmaSalesEstimator'],
    packages = find_packages(),
    include_package_data = True,
)