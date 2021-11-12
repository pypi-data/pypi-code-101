from distutils.core import setup

setup(
    name='ds-my-tools',
    version='0.0.4',
    py_modules=['my_tools'],
    author='lideshan',
    author_email='leebigshan@gmail.com',
    url='',
    description='',
    classifiers=[  # 这里我们指定证书, python版本和系统类型
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # 这里指定python版本号必须大于3.6才可以安装
    install_requires=['pymupdf', 'requests']
)
