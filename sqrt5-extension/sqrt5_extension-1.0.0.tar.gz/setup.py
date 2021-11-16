from setuptools import setup

setup(
    name='sqrt5_extension',
    version='1.0.0',
    description='useful tools',
    author='Sqrt5',
    author_email='2.236068@gmail.com',
    url='https://www.python.org/',
    license='MIT',
    packages=['extension'],
    install_requires=[
        # utils, utilsImage, utilsLabel need
        'Pillow>=8.1.0',
        'numpy>=1.18.2',
        'opencv-contrib-python-headless>=4.5.2',
        'pytz',
        # GFS need
        'pymongo>=3.11.4',
        # baseLMDB, normalLMDB, imageLMDB need
        'lmdb>=1.2.1'
    ],
    python_requires='>=3',
    include_package_data=True
)
