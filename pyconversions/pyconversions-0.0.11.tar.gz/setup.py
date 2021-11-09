from setuptools import setup, find_packages

VERSION = '0.0.11'
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
                   "\n Other than Unit Lengths the ones added in the package are \n" \
                   "* Fahrenheit \n" \
                   "* Celsius \n" \
                   "\n For starters, import the class as shown below: \n" \
                   "* import pyconversions.pyconv as pycv " \
                   "\n After that for an instance lets say to convert 12 Inches to Meters use: \n" \
                   "* pycv.Inches(12).toMeters() \n" \
                   "\n Or to convert 12 Meters to Centimeters use: \n" \
                   "* pycv.Meters(12).toCentimeters() \n" \
                   "\n Just like for for Unit Lengths, you can use it for Temperatures too as follows:\n" \
                   "* pycv.Fahrenheit(35).toCelcius() \n" \
                   "\n Or to convert it vice-versa use: \n" \
                   "* pycv.Celcius(68).toFahrenheit"

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
