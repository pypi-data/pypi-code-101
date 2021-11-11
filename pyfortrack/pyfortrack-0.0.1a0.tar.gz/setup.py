from setuptools import find_packages, setup, Extension
from Cython.Build import cythonize

#    ext_modules=[Extension('py4track/py4track_runner', ['py4track/__main__.c','py4track/fib.c'])],
setup(
    name='pyfortrack',
    version='0.0.1a0',
    description='Python for Track',
    url='http://github.com/py4track',
    author=u'Helvecio Neto',
    author_email='helvecio.neto@inpe.br',
    license='GPL',
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3.8",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Utilities",
    ],
    keywords='track',
    install_requires=['numpy'],
    data_files=[('pyfortrack',['data/data.txt'])],
    packages=find_packages(),
    zip_safe=True
    )