from setuptools import setup, find_packages

VERSION = '0.0.5'
DESCRIPTION = 'Convert Unit Length Datas'
LONG_DESCRIPTION = "Convert all types of Unit Length Datas. The one's in this Package are " \
                   "* Inches" \
                   "* Feet" \
                   "* Yard" \
                   "* Millimeter" \
                   "* Centimeter" \
                   "* Decimeter" \
                   "* Decameter" \
                   "* Hectometer" \
                   "* Meter" \
                   "* Kilometer" \
                   "Other than Unit Lengths the ones added in the package are" \
                   "* Fahrenheit" \
                   "* Celsius" \
                   "To convert a certain Unit Data or Temperature use:" \
                   "* import pyconversions.pyconv as pycv * " \
                   "and after that for an instance to convert 12 Inches to Meters use: " \
                   "* pycv.Inches(12).toMeters() *" \
                   " or to convert 12 Meters to Centimeters use: " \
                   "* pycv.Meters(12).toCentimeters()* "\

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
