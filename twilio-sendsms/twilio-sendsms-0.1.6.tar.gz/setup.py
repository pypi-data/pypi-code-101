import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="twilio-sendsms",
    version="0.1.6",
    author="Cormac O'Mahony",
    author_email="cormac@omahony.id.au",
    description="A utility for sending SMS using a mustache temlate",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/omahoco/twilio-sendsms",
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts':
            ["sendsms=twilio_sendsms.sendsms:main"]
    },
    # scripts=['twilio-sendsms'],
    install_requires=['pandas', 'pystache',
                      'twilio', 'InquirerPy'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
