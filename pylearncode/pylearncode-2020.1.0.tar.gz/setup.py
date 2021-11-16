import setuptools

# pip install twine wheel
# python setup.py sdist bdist_wheel
# twine upload dist/* -u VicWang -p PYPI******

setuptools.setup(
    name="pylearncode",
    version="2020.1.0",
    author="Himansh Raj",
    author_email="iamthehimansh@gmail.com",
    description='A simple 2D game engine base on pyglet',
    long_description='A simple 2D game engine base on pyglet',
    long_description_content_type="text/markdown",
    url='http://github.com/iamthehimansh/PyLearnCode',
    download_url="https://github.com/iamthehimansh/PyLearnCode/archive/refs/tags/2020.1.0.tar.gz",
    packages=setuptools.find_packages(),
    install_requires=[
        'pyglet==1.3.2'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
)
#leaptask>=2020.3.27