import setuptools

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

# https://github.com/Naereen/badges
# https://www.alura.com.br/artigos/como-publicar-seu-codigo-python-no-pypi

# python setup.py sdist
# twine upload dist/* --repository-url https://test.pypi.org/legacy/

setuptools.setup(
    name='heuristic',
    version='0.0.2',
    author='João Vitor Coelho Estrela',
    author_email='jvitorestrella@gmail.com',
    description='Optimization package with wide flexibility for logical understanding',
    #long_description=long_description,
    #long_description_content_type='text/markdown',
    #url='https://github.com/pypa/sampleproject',
    packages=setuptools.find_packages(),
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering',
        'Topic :: Education'
    ],
    python_requires='>=3.6',
)