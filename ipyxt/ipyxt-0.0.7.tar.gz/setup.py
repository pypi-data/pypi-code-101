from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='ipyxt',
    version='0.0.7',
    description='IPython extensions',
    long_description_content_type='text/markdown',
    long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Esteban Uri',
    author_email='estebanuri@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='ipython extensions',
    packages=find_packages(),
    package_data={'': ['ding.mp3', 'error.mp3']},
    include_package_data=True,
    install_requires=[]
)