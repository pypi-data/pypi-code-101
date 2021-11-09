from setuptools import setup, find_packages

VERSION = '0.0.6'
DESCRIPTION = 'Convert Unit Length Datas'
LONG_DESCRIPTION = "Convert all types of Unit Length Datas. The one's in this Package are \n" \
                   "* Inches \n" \
                   "* Feet \n" \
                   "* Yard \n" \
                   "* Millimeter \n" \
                   "* Centimeter \n" \
                   "* Decimeter \n" \
                   "* Decameter \n" \
                   "* Hectometer \n" \
                   "* Meter \n" \
                   "* Kilometer \n" \
                   "Other than Unit Lengths the ones added in the package are \n" \
                   "* Fahrenheit \n" \
                   "* Celsius \n" \
                   "To convert a certain Unit Data or Temperature use:\n" \
                   "* import pyconversions.pyconv as pycv * \n" \
                   "and after that for an instance to convert 12 Inches to Meters use: \n" \
                   "* pycv.Inches(12).toMeters() * \n" \
                   " or to convert 12 Meters to Centimeters use: \n" \
                   "* pycv.Meters(12).toCentimeters()* \n"\

# Setting up
setup(
    name="pyconversions",
    version=VERSION,
    author="Logan",
    author_email="<lgnx@gnamil.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'unitlength', 'length', 'distances', 'diameters', 'meters'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
