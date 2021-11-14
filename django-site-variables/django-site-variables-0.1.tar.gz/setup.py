from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='django-site-variables',
    version='0.1',
    packages=['django_site_variables', 'django_site_variables.migrations'],
    url='',
    license='MIT',
    author='Mikhail Badrazhan',
    author_email='svne@devilweb.ru',
    description='Site variables application',
    include_package_data=True,
    package_data={
        'django_site_variables': [
            'django_site_variables/locale/*/LC_MESSAGES/*.mo',
            'django_site_variables/locale/*/LC_MESSAGES/*.po',
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires='>=3.6',
    long_description=long_description,
    install_requires=[
        'django'
    ],
    long_description_content_type="text/markdown",
)
