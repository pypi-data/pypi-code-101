from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

install_requires = [
    "gql[all]==v3.0.0a5",
    "websockets==8.1",
    "dataclasses-json==0.5.2",
    "pendulum==2.1.2",
    "pycryptodome==3.10.1",
    "eth-keys==0.3.3",
    "py-dotenv==0.1"
]

tests_requires = [
    "pytest==6.2.2",
    "pytest-cov==2.11.1"
]

dev_requires = [
    "twine==3.4.1",
    "build==0.3.1"
]

setup(
    name="ew_dsb_client_lib",
    version="0.1.2a1",
    author="Pablo Buitrago",
    author_email="messaging@energyweb.org",
    description="Python client library for the EW-SMS module",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/energywebfoundation/sms-client-lib-py.git",
    project_urls={
        "Bug Tracker": "https://github.com/energywebfoundation/sms-client-lib-py/issues",
    },
    license='LICENSE',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
    keywords="ethereum decentralised energy-web pubsub messaging",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.7",
    install_requires=install_requires,
    tests_require=install_requires + tests_requires,
    extras_require={
        "all": install_requires + tests_requires + dev_requires,
        "test": install_requires + tests_requires
    }
)