from setuptools import setup, find_packages

setup(
    name = "waste_simulation",
    version ="0.0.1",
    author = "Justin Rush",
    url="",
    author_email="jandrewrush@gmail.com",
    description = "",
    py_modules=["waste_simulation","helpers","base"],
    package_dir={'':'src'},
    install_requires = ["pandas"]

   
    
)

