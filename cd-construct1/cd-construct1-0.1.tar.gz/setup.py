import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='cd-construct1',  
     version='0.1',
     author="Wolfgang Unger",
     author_email="wolfgang.r.unger@gmail.com",
     description="A Test package",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/javatechy/dokr",
     #packages=setuptools.find_packages(),
     packages=['cdk_construct1'],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )