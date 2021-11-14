from setuptools import setup

setup(
    name='scgc',
    version='0.3.0',
    description='SCGC sequence processing, pipelines, and utilities',
    long_description=open('README.rst').read(),
    author='Joe Brown',
    author_email='jmbrown@bigelow.org',
    license='MIT',
    url='https://github.com/BigelowLab/scgcpy',
    packages=['scgc'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'click',
        'click-config',
        'interlap',
        # 'matplotlib',
        'numpy',
        'pandas',
        'parmap',
        'pysam',
        'sarge',
        # 'seaborn',
        'toolshed',
    ],
    entry_points='''
        [console_scripts]
        scgc=scgc.__main__:cli
    ''',
    classifiers=[
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Utilities',
    ],
)
