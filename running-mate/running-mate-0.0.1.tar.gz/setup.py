import setuptools

setuptools.setup(
    name="running-mate",
    version="0.0.1",
    author="Michael Herman",
    author_email="michael@mherman.org",
    description="Lightweight MLOps framework.",
    url="https://github.com/mjhea0/running-mate",
    packages=setuptools.find_packages(),
    install_requires=[
        "dacite==1.6.0",
        "numpy==1.21.3",
        "pandas==1.3.4",
        "requests==2.26.0",
    ],
)
