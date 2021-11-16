import setuptools

with open("README.md", "r", encoding="utf-8") as README:
    long_description = README.read()

setuptools.setup(
    name='csv2pdf',
    version='0.1.3',
    description='Easily convert CSV Files to PDF Files using Python!',
    author= 'SOHAM DATTA',
    author_email='dattasoham805@gmail.com',
    url = 'https://github.com/TECH-SAVVY-GUY/csv2pdf',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    keywords=['csv', 'pdf', 'csv2pdf', 'converter', 'file-converter'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    py_modules=['csv2pdf'],
    package_dir={'':'src'},
    install_requires = [
        'fpdf2'
    ]
)