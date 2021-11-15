from setuptools import setup


setup(
    name='clevr',
    version='0.5',
    description='Official Python SDK for Clevr.',
    long_description='Please visit https://beta.clevr-ai.com/docs for API examples and documentation.',
    py_modules=['clevr'],
    install_requires=[
             'Pillow>=7.1',
             'requests>=2.26'       
    ],
    license='MIT',
    package_dir={'': 'clevr'}
)