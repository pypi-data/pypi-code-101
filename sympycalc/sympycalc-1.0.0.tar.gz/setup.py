from setuptools import setup, find_packages
  
long_description = 'Simple commandline calculator'
  
setup(
        name ='sympycalc',
        version ='1.0.0',
        author ='Harish PVV',
        author_email ='harishpvv@gmail.com',
        description ='Simple commandline calculator',
        long_description = long_description,
        long_description_content_type ="text/markdown",
        license ='MIT',
        packages = find_packages(),
        entry_points ={
            'console_scripts': [
                'sympycalc = src.sympycalc:main',
                'pc = src.sympycalc:main'
            ]
        },
        classifiers =(
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ),
        keywords ='calculator commandline terminal harishpvv',
        install_requires = ['sympy'],
        zip_safe = False
)
