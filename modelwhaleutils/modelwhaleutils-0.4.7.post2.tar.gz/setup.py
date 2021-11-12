import setuptools

setuptools.setup(
    name="modelwhaleutils",
    version="0.4.7-post2",
    author="modalwhale team",
    description="use in mw",
    url="https://github.com/gerard0315/mwutils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["PyJWT", "requests", "pynvml", "psutil"],
    python_requires='>=3.6',
)
